import base64
import datetime
import os
import re
import io
import shutil
import smtplib
import traceback
import zipfile
from time import sleep
from pprint import pprint
from email.header import Header
from email.mime.application import MIMEApplication  # 发送附件
from email.mime.multipart import MIMEMultipart  # 发送多个部分
from email.mime.text import MIMEText  # 专门发送正文
from smb.SMBConnection import SMBConnection
from smb.smb_structs import OperationFailure
import requests
import urllib3

import uuid
from smbprotocol.connection import Connection
from smbprotocol.session import Session
from smbprotocol.tree import TreeConnect
from smbprotocol.open import Open
from smbprotocol.file_info import FileInformationClass

from urllib3.exceptions import InsecureRequestWarning
from BoschRpaMagicBox.common_functions import WebSapCommonFunctions

urllib3.disable_warnings(InsecureRequestWarning)


def create_error_log(error_log_folder_path: str, error_info: str):
    """This function is used to create error log when there is an error occurred during RPA operation

    Args:
        error_log_folder_path(str): This is the path of folder to save error logs
        error_info(str): This is the error message that need to be added to error log
    """

    if not os.path.exists(error_log_folder_path):
        os.mkdir(error_log_folder_path)

    time_in_path = str(datetime.datetime.now().date())
    with open(error_log_folder_path + os.sep + f'error_log_{time_in_path}.txt', 'a', encoding='utf-8') as file:
        file.write('{time}\n'.format(time=datetime.datetime.now()))
        file.write(error_info)
        file.write('\n')


def print_webpage_as_pdf(web_rpa: WebSapCommonFunctions, save_file_path: str):
    """This function is used to

    Args:
        web_rpa(WebSapCommonFunctions): This is the instance of WebSapCommonFunctions
        save_file_path(str): This is the file path to save
    """
    webpage_content = web_rpa.browser.print_page()

    with open(save_file_path, 'wb') as file:
        file.write(base64.b64decode(webpage_content))


def send_email_by_server(nt_account: str, email_password: str, email_address: str, email_body: str, email_header: str, email_subject: str,
                         email_to: list, email_cc: list, attachment_dict: dict, error_log_folder_path: str):
    """This function is used to send emails

    Args:
        nt_account(str): This is the nt account of user
        email_password(str): This is the email password for nt account
        email_address(str): This is the email address of nt account
        email_body(str): This is the email content
        email_header(str): This is the customized sender name instead of actual user nt
        email_subject(str): This is the email subject
        email_to(list): This is the list of to emails
        email_cc(list): This is the list of cc emails
        attachment_dict(dict): This is the dict of attachment info. r.g. {file name： file path}
        error_log_folder_path(str): This is the folder path for saving error log
    """
    mail_host = 'rb-smtp-auth.rbesz01.com'
    # outlook用户名
    mail_user = f'APAC\\{nt_account}'
    # 密码(部分邮箱为授权码)
    mail_pass = f'{email_password}'
    # 邮件发送方邮箱地址
    sender = email_address

    try:
        smtpObj = smtplib.SMTP(mail_host, 25)
        # 连接到服务器
        # smtpObj.connect(mail_host, 25)
        smtpObj.starttls()
        # 登录到服务器
        smtpObj.login(mail_user, mail_pass)
        # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
        receivers = ','.join(email_to)
        ccs = ','.join(email_cc)

        # 设置email信息
        # 邮件内容设置
        message = MIMEMultipart()
        # 邮件主题

        # 发送方信息
        message['From'] = Header(email_header, 'utf-8')
        # 接受方信息
        message['To'] = receivers
        message['Cc'] = ccs

        message['Subject'] = email_subject
        content = MIMEText(email_body, 'html', 'utf-8')
        message.attach(content)
        # 添加附件
        for file_name, file_path in attachment_dict.items():
            if os.path.exists(file_path):
                with open(file_path, 'rb') as file:
                    content = file.read()
                att = MIMEApplication(content)
                att.add_header('Content-Disposition', 'attachment', filename=file_name)  # 为附件命名
                message.attach(att)

        # 发送
        smtpObj.sendmail(from_addr=sender, to_addrs=email_to + email_cc, msg=message.as_string())

        # 退出
        smtpObj.quit()
        print(f'-----email is sent successfully!-----')
    except:
        print('Mail sent failed.')
        create_error_log(error_log_folder_path, traceback.format_exc())


def transform_amount_into_float_format(str_amount: str, precision=2):
    """This function is used to transform str amount into float format

    Args:
        precision(int): This is the precision requirement
        str_amount(str): This is the amount in string format
    """
    str_amount = str_amount.replace(',', '').replace('，', '').replace('(', '-').replace('（', '-').replace(')', '').replace('）', '')
    if str_amount:
        if str_amount != '-':
            float_amount = round(float(str_amount), precision)
        else:
            float_amount = 0
    else:
        float_amount = 0
    return float_amount


def get_chrome_browser_version(chrome_error_message):
    """This function is used to extract Chrome version info

    Args:
        chrome_error_message(str): This is the error message from exception to SessionNotCreatedException
    """
    chrome_version = ''
    current_version_list = re.findall('.*?Current browser version is (.*?) with binary pfath.*', chrome_error_message)
    if current_version_list:
        chrome_version = current_version_list[0]
    else:
        current_version_list = re.findall('(\d+\.\d+\.\d+\.\d+)', chrome_error_message)
        if current_version_list:
            chrome_version = current_version_list[0]
    return chrome_version


def unzip_chrome_driver(target_file_path, target_folder_path, win_type):
    """This function is used to unzip Chrome driver zip file

    Args:
        target_file_path(str): This the file path of chromedriver.exe
        target_folder_path(str): This is the folder to save chromedriver.exe
        win_type(str): win64 or win32
    """
    existed_file_path = target_folder_path + os.sep + 'chromedriver.exe'
    existed_folder_path = target_folder_path + os.sep + f'chromedriver-{win_type}'
    if os.path.exists(existed_file_path):
        os.remove(existed_file_path)

    if os.path.exists(existed_folder_path):
        shutil.rmtree(existed_folder_path)

    zip_file = zipfile.ZipFile(target_file_path)
    zip_file.extractall(path=target_folder_path)
    zip_file.close()
    sleep(1)
    shutil.move(existed_folder_path + os.sep + 'chromedriver.exe', existed_file_path)


def download_chrome_driver(target_driver_version_list):
    """This function is used to download Chrome driver

    Args:
        target_driver_version_list(list[dict]): This is the list of chrome driver

    """
    is_successful = False
    download_url_dict = {}
    win_type = ''
    current_date = datetime.datetime.now().date()
    for chrome_driver_info in target_driver_version_list:
        if chrome_driver_info['platform'] == 'win64':
            download_url_dict['win64'] = chrome_driver_info['url']
            win_type = 'win64'
        if chrome_driver_info['platform'] == 'win32':
            download_url_dict['win32'] = chrome_driver_info['url']
            win_type = 'win32'
    if download_url_dict.get('win64'):
        download_url = download_url_dict.get('win64')
    elif download_url_dict.get('win32'):
        download_url = download_url_dict.get('win32')
    else:
        download_url = ''

    if download_url:
        print(f'download_url: {download_url}')
        res = requests.get(download_url, timeout=None)
        with open(f'chrome_driver_{current_date}.zip', 'wb') as file:
            file.write(res.content)

        target_file_path = os.getcwd() + os.sep + f'chrome_driver_{current_date}.zip'
        target_folder_path = os.getcwd()
        unzip_chrome_driver(target_file_path, target_folder_path, win_type)
        is_successful = True
    return is_successful


def auto_update_chrome_driver(chrome_driver_version):
    """This function is used to auto download chrome  driver

    Args:
        chrome_driver_version(str): This is the version of  chrome driver

    """
    is_successful = False
    if chrome_driver_version:
        res = requests.get('https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json')
        res_json = res.json()
        chrome_versions = res_json['versions']

        target_version_list = []
        target_driver_version_list = []

        cv1, cv2, cv3, cv4 = [int(v) for v in chrome_driver_version.split('.')]
        for chrome_version_dict in chrome_versions:
            chrome_version = chrome_version_dict['version']
            chrome_driver_list = chrome_version_dict.get('downloads', {'chromedriver': []}).get('chromedriver', [])
            v1, v2, v3, v4 = [int(v) for v in chrome_version.split('.')]
            if chrome_driver_list and v1 == cv1 and v2 == cv2 and v3 <= cv3 and v4 <= cv4:
                if target_version_list:
                    if (v1 >= target_version_list[0]
                            and v2 >= target_version_list[1]
                            and v3 >= target_version_list[2]
                            and v4 >= target_version_list[3]):
                        target_version_list = [v1, v2, v3, v4]
                        target_driver_version_list = chrome_driver_list
                else:
                    target_version_list = [v1, v2, v3, v4]
                    target_driver_version_list = chrome_driver_list
        pprint(target_driver_version_list)
        if target_driver_version_list:
            is_successful = download_chrome_driver(target_driver_version_list)

    return is_successful


def smb_copy_file_local_to_remote(username, password, server_ip, server_name, share_name, local_file_path, remote_file_path, port):
    """ This function is used to copy local file to public folder

    Args:
        username(str): This is the username
        password(str): This is the password
        server_ip(str): This is the ip address of the public folder, which can be same as server name
        server_name(str):This is the server name (url), e.g. szh0fs06.apac.bosch.com
        share_name(str): This is the share_name of public folder, e.g. GS_ACC_CN$
        local_file_path(str): This is the local file path
        remote_file_path(str): This is the public file path that file will be saved under share name folder
        port(int): This is the port number of the server name
    """
    conn = SMBConnection(username, password, username, server_name, use_ntlm_v2=True, is_direct_tcp=True)
    assert conn.connect(server_ip, port)

    with open(local_file_path, 'rb') as file:
        file_obj = io.BytesIO(file.read())
        conn.storeFile(share_name, remote_file_path, file_obj)
        file_obj.close()

    conn.close()


def smb_store_remote_file_by_obj(username, password, server_ip, server_name, share_name, remote_file_path, file_obj, port):
    """ This function is used to store file to public folder

    Args:
        file_obj(io.BytesIO): This is the file object
        username(str): This is the username
        password(str): This is the password
        server_ip(str): This is the ip address of the public folder, which can be same as server name
        server_name(str):This is the server name (url), e.g. szh0fs06.apac.bosch.com
        share_name(str): This is the share_name of public folder, e.g. GS_ACC_CN$
        remote_file_path(str): This is the public file path that file will be saved under share name folder
        port(int): This is the port number of the server name
    """
    conn = SMBConnection(username, password, username, server_name, use_ntlm_v2=True, is_direct_tcp=True)
    assert conn.connect(server_ip, port)

    conn.storeFile(share_name, remote_file_path, file_obj)
    conn.close()


def smb_check_file_exist(username, password, server_ip, server_name, share_name, remote_file_path, port):
    """ This function is used to check whether remote file is existed

    Args:
        username(str): This is the username
        password(str): This is the password
        server_ip(str): This is the ip address of the public folder, which can be same as server name
        server_name(str):This is the server name (url), e.g. szh0fs06.apac.bosch.com
        share_name(str): This is the share_name of public folder, e.g. GS_ACC_CN$
        remote_file_path(str): This is the public file path that file will be saved under share name folder
        port(int): This is the port number of the server name
    """
    conn = SMBConnection(username, password, username, server_name, use_ntlm_v2=True, is_direct_tcp=True)
    assert conn.connect(server_ip, port)
    is_file_exist = True

    file_obj = io.BytesIO()
    try:
        conn.retrieveFile(share_name, remote_file_path, file_obj)
        file_obj.seek(0)
    except OperationFailure:
        is_file_exist = False
    finally:
        conn.close()

    return is_file_exist, file_obj


def smb_check_folder_exist(username, password, server_ip, server_name, share_name, remote_folder_path, port):
    """ This function is used to check whether remote folder is existed

    Args:
        username(str): This is the username
        password(str): This is the password
        server_ip(str): This is the ip address of the public folder, which can be same as server name
        server_name(str):This is the server name (url), e.g. szh0fs06.apac.bosch.com
        share_name(str): This is the share_name of public folder, e.g. GS_ACC_CN$
        remote_folder_path(str): This is the public folder path that folder will be saved under share name folder
        port(int): This is the port number of the server name
    """
    conn = SMBConnection(username, password, username, server_name, use_ntlm_v2=True, is_direct_tcp=True)
    assert conn.connect(server_ip, port)
    is_folder_exist = True
    try:
        # 尝试列出目录内容
        conn.listPath(share_name, remote_folder_path)
    except OperationFailure:
        is_folder_exist = False
    finally:
        conn.close()

    return is_folder_exist


def smb_traverse_remote_folder(username, password, server_ip, server_name, share_name, remote_folder_path, port):
    """ This function is list all files or folders within remote folder

    Args:
        username(str): This is the username
        password(str): This is the password
        server_ip(str): This is the ip address of the public folder, which can be same as server name
        server_name(str):This is the server name (url), e.g. szh0fs06.apac.bosch.com
        share_name(str): This is the share_name of public folder, e.g. GS_ACC_CN$
        remote_folder_path(str): This is the public folder path that folder will be saved under share name folder
        port(int): This is the port number of the server name
    """

    traverse_result_list = []
    client_guid = uuid.uuid4()
    connection = Connection(guid=client_guid, server_name=server_ip, port=445)
    connection.connect()

    session = Session(connection, username, password)
    session.connect()

    tree = TreeConnect(session, f"\\\\{server_ip}\\{share_name}")
    tree.connect()

    folder_open = Open(tree, remote_folder_path)
    folder_open.create(impersonation_level=0,
                       desired_access=0x00000001,  # read only
                       file_attributes=0,
                       share_access=0x00000001,  # allow other process
                       create_disposition=1,  # OPEN_EXISTING
                       create_options=0
                       )
    try:
        pattern = "*"  # match all
        file_information_class = FileInformationClass.FILE_DIRECTORY_INFORMATION
        file_info = folder_open.query_directory(pattern, file_information_class)
        for item in file_info:
            item_name = item.fields.get('file_name').value.decode('utf-16')
            if item_name not in ['.', '..']:
                creation_time = item.fields.get('creation_time').value
                last_access_time = item.fields.get('last_access_time').value
                last_write_time = item.fields.get('last_write_time').value
                change_time = item.fields.get('change_time').value

                if item.fields.get('file_attributes').value & 0x10:  # check whether item is folder
                    traverse_result_list.append({'name': item_name,
                                                 'is_folder': True, 'is_file': False, 'creation_time': creation_time, 'last_access_time': last_access_time,
                                                 'last_write_time': last_write_time, 'change_time': change_time})
                else:
                    traverse_result_list.append({'name': item_name,
                                                 'is_folder': False, 'is_file': True, 'creation_time': creation_time, 'last_access_time': last_access_time,
                                                 'last_write_time': last_write_time, 'change_time': change_time})
    finally:
        connection.disconnect()
        session.disconnect()
        tree.disconnect()

    return traverse_result_list


def smb_copy_file_remote_to_local(username, password, server_ip, server_name, share_name, local_file_path, remote_file_path, port):
    """ This function is used to copy local file to public folder

    Args:
        username(str): This is the username
        password(str): This is the password
        server_ip(str): This is the ip address of the public folder, which can be same as server name
        server_name(str):This is the server name (url), e.g. szh0fs06.apac.bosch.com
        share_name(str): This is the share_name of public folder, e.g. GS_ACC_CN$
        local_file_path(str): This is the local file path
        remote_file_path(str): This is the public file path that file will be saved under share name folder
        port(int): This is the port number of the server name
    """
    # 建立连接
    conn = SMBConnection(username, password, username, server_name, use_ntlm_v2=True, is_direct_tcp=True)
    assert conn.connect(server_ip, port)

    with open(local_file_path, 'wb') as file_obj:
        conn.retrieveFile(share_name, remote_file_path, file_obj)
        file_obj.close()

    # 断开连接
    conn.close()


def smb_load_file_obj(username: str, password: str, server_ip: str, server_name: str, share_name: str, remote_file_path: str, port: int = 445):
    """ This function is used to get file object from public folder

    Args:
        username(str): This is the username
        password(str): This is the password
        server_ip(str): This is the ip address of the public folder, which can be same as server name
        server_name(str):This is the server name (url), e.g. szh0fs06.apac.bosch.com
        share_name(str): This is the share_name of public folder, e.g. GS_ACC_CN$
        remote_file_path(str): This is the public file path that file will be saved under share name folder
        port(int): This is the port number of the server name
    """
    # 建立连接
    conn = SMBConnection(username, password, username, server_name, use_ntlm_v2=True, is_direct_tcp=True)
    assert conn.connect(server_ip, port)

    file_obj = io.BytesIO()
    conn.retrieveFile(share_name, remote_file_path, file_obj)
    file_obj.seek(0)

    # 断开连接
    conn.close()

    return file_obj


def smb_delete_file(username, password, server_ip, server_name, share_name, remote_file_path, port=445):
    """ This function is used to copy local file to public folder

    Args:
        username(str): This is the username
        password(str): This is the password
        server_ip(str): This is the ip address of the public folder, which can be same as server name
        server_name(str):This is the server name (url), e.g. szh0fs06.apac.bosch.com
        share_name(str): This is the share_name of public folder, e.g. GS_ACC_CN$
        remote_file_path(str): This is the public file path that file will be saved under share name folder
        port(int): This is the port number of the server name
    """
    is_file_exist = smb_check_file_exist(username, password, server_ip, server_name, share_name, remote_file_path, port)
    if is_file_exist:
        conn = SMBConnection(username, password, username, server_name, use_ntlm_v2=True, is_direct_tcp=True)
        assert conn.connect(server_ip, port)

        conn.deleteFiles(share_name, remote_file_path)

        conn.close()


def smb_create_folder(username, password, server_ip, server_name, share_name, remote_folder_path, port=445):
    """ This function is used to copy local file to public folder

    Args:
        username(str): This is the username
        password(str): This is the password
        server_ip(str): This is the ip address of the public folder, which can be same as server name
        server_name(str):This is the server name (url), e.g. szh0fs06.apac.bosch.com
        share_name(str): This is the share_name of public folder, e.g. GS_ACC_CN$
        remote_folder_path(str): This is the public folder path that folder will be created under share name folder
        port(int): This is the port number of the server name
    """

    is_folder_exist = smb_check_folder_exist(username, password, server_ip, server_name, share_name, remote_folder_path, port)
    if is_folder_exist:
        conn = SMBConnection(username, password, username, server_name, use_ntlm_v2=True, is_direct_tcp=True)
        assert conn.connect(server_ip, port)
        try:
            conn.createDirectory(share_name, remote_folder_path)
        except OperationFailure:
            pass

        conn.close()


def get_bot_variants(bot_url):
    """ This function is used to get bot variants

    Args:
        bot_url(str): This is the url of bot
    """
    container_name = os.environ.get('CONTAINER_NAME', '')
    api_file_path = f'/bot_tasks/{container_name}/Code_Folder/VARIANT_API_SECRET.txt'

    if os.path.exists(api_file_path):
        with open(api_file_path, 'r', encoding='utf-8') as api_file:
            api_secret = api_file.read().strip()

        if api_secret:
            request_data = {
                "queryType": "get_bot_variants",
                "apiCredential": api_secret,
            }
            res = requests.post(url=bot_url, data=request_data, verify=False)
            try:
                bot_variant_dict = res.json()['data']
                return bot_variant_dict
            except:
                return {}
        else:
            return {}

    else:
        return {}
