# -*- coding: utf-8 -*-
"""
@File     : FlexiSpiderTools
@Author   : chengming
@Email    : chengming0412@gmail.com
@Date     : 2024/10/22 17:32
@Blog     : https://blog.chengmingfun.com
@Copyright: © 2024 Your Company. All rights reserved.
"""
import base64
import hashlib
import os
import random
import re
import socket
import string
import sys
import time
import urllib.parse
import uuid
from urllib import request

from loguru import logger
from faker import Faker
import requests


class FlexiTools:
    def __init__(self):
        self.fake = Faker('zh_CN')

    def random_name(self):
        """生成随机姓名"""
        return self.fake.name()

    def random_phone_number(self):
        """生成随机手机号"""
        return self.fake.phone_number()

    def random_id_number(self):
        """生成随机身份证号"""
        return self.fake.ssn()

    def md5_encrypt(self, data):
        """
        MD5加密
        :param data: 需要加密的数据
        :return:
        """
        return hashlib.md5(data.encode()).hexdigest()

    def base64_encode(self, data):
        """
        Base64加密
        :param data: 需要加密的数据
        :return:
        """
        return base64.b64encode(data)

    def base64_decode(self, data):
        """
        Base64解密
        :param data: 需要解密的数据
        :return:
        """
        return base64.b64decode(data)

    def cookiesjar2str(self, cookies):
        """
        requests 库获取的 cookies 直接转换为字符串格式
        :param cookies: 传入一个 CookieJar 对象
        :return:
        """
        str_cookie = ""
        for k, v in requests.utils.dict_from_cookiejar(cookies).items():
            str_cookie += k
            str_cookie += "="
            str_cookie += v
            str_cookie += "; "
        return str_cookie

    def urlencode(self, params):
        """
        字典类型的参数转为字符串
        @param params:
        {
            'a': 1,
            'b': 2
        }
        @return: a=1&b=2
        """
        return urllib.parse.urlencode(params)

    def urldecode(self, url):
        """
        将字符串类型的参数转为json
        @param url: xxx?a=1&b=2
        @return:
        {
            'a': 1,
            'b': 2
        }
        """
        params_json = {}
        params = url.split("?")[-1].split("&")
        for param in params:
            key, value = param.split("=", 1)
            params_json[key] = self.unquote_url(value)

        return params_json

    def unquote_url(self, url, encoding="utf-8"):
        """
        @summary: 将url解码
        ---------
        @param url:
        ---------
        @result:
        """

        return urllib.parse.unquote(url, encoding=encoding)

    def quote_url(self, url, encoding="utf-8"):
        """
        @summary: 将url编码 编码意思http://www.w3school.com.cn/tags/html_ref_urlencode.html
        ---------
        @param url:
        ---------
        @result:
        """

        return urllib.parse.quote(url, safe="%;/?:@&=+$,", encoding=encoding)

    def get_localhost_ip(self):
        """
        利用 UDP 协议来实现的，生成一个UDP包，把自己的 IP 放如到 UDP 协议头中，然后从UDP包中获取本机的IP。
        这个方法并不会真实的向外部发包，所以用抓包工具是看不到的
        :return:
        """
        s = None
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
        except:
            ip = ""
        finally:
            if s:
                s.close()

        return ip

    def is_valid_proxy(self, proxy, check_url=None):
        """
        检验代理是否有效
        @param proxy: xxx.xxx.xxx:xxx
        @param check_url: 利用目标网站检查，目标网站url。默认为None， 使用代理服务器的socket检查, 但不能排除Connection closed by foreign host
        @return: True / False
        """
        is_valid = False

        if check_url:
            proxies = {"http": f"http://{proxy}", "https": f"https://{proxy}"}
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
            }
            response = None
            try:
                response = requests.get(
                    check_url, headers=headers, proxies=proxies, stream=True, timeout=20
                )
                is_valid = True

            except Exception as e:
                logger.error(f"check proxy failed: {e} {proxy}")

            finally:
                if response:
                    response.close()

        else:
            ip, port = proxy.split(":")
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sk:
                sk.settimeout(7)
                try:
                    sk.connect((ip, int(port)))  # 检查代理服务器是否开着
                    is_valid = True

                except Exception as e:
                    logger.error(f"check proxy failed: {e} {ip}:{port}")

        return is_valid

    def is_valid_url(self, url):
        """
        验证url是否合法
        :param url:
        :return:
        """
        if re.match(r"(^https?:/{2}\w.+$)|(ftp://)", url):
            return True
        else:
            return False

    def mkdir(self, path):
        try:
            if not os.path.exists(path):
                os.makedirs(path)
        except OSError as exc:  # Python >2.5
            pass

    def write_file(self, filename, content, mode="w", encoding="utf-8"):
        """
        @summary: 写文件
        ---------
        @param filename: 文件名（有路径）
        @param content: 内容
        @param mode: 模式 w/w+ (覆盖/追加)
        ---------
        @result:
        """

        directory = os.path.dirname(filename)
        self.mkdir(directory)
        with open(filename, mode, encoding=encoding) as file:
            file.writelines(content)

    def read_file(self, filename, readlines=False, encoding="utf-8"):
        """
        @summary: 读文件
        ---------
        @param filename: 文件名（有路径）
        @param readlines: 按行读取 （默认False）
        ---------
        @result: 按行读取返回List，否则返回字符串
        """

        content = None
        try:
            with open(filename, "r", encoding=encoding) as file:
                content = file.readlines() if readlines else file.read()
        except Exception as e:
            logger.error(e)

        return content

    def download_file(self, url, file_path, *, call_func=None, proxies=None, data=None):
        """
        下载文件，会自动创建文件存储目录
        Args:
            url: 地址
            file_path: 文件存储地址
            call_func: 下载成功的回调
            proxies: 代理
            data: 请求体

        Returns:

        """
        directory = os.path.dirname(file_path)
        self.mkdir(directory)

        # 进度条
        def progress_callfunc(blocknum, blocksize, totalsize):
            """回调函数
            @blocknum : 已经下载的数据块
            @blocksize : 数据块的大小
            @totalsize: 远程文件的大小
            """
            percent = 100.0 * blocknum * blocksize / totalsize
            if percent > 100:
                percent = 100
            # print ('进度条 %.2f%%' % percent, end = '\r')
            sys.stdout.write("进度条 %.2f%%" % percent + "\r")
            sys.stdout.flush()

        if url:
            try:
                if proxies:
                    # create the object, assign it to a variable
                    proxy = request.ProxyHandler(proxies)
                    # construct a new opener using your proxy settings
                    opener = request.build_opener(proxy)
                    # install the openen on the module-level
                    request.install_opener(opener)

                request.urlretrieve(url, file_path, progress_callfunc, data)

                if callable(call_func):
                    call_func()
                return 1
            except Exception as e:
                logger.error(e)
                return 0
        else:
            return 0

    def date_to_timestamp(self, date, time_format="%Y-%m-%d %H:%M:%S"):
        """
        @summary:
        ---------
        @param date:将"2011-09-28 10:00:00"时间格式转化为时间戳
        @param format:时间格式
        ---------
        @result: 返回时间戳
        """

        timestamp = time.mktime(time.strptime(date, time_format))
        return int(timestamp)

    def timestamp_to_date(self, timestamp, time_format="%Y-%m-%d %H:%M:%S"):
        """
        @summary:
        ---------
        @param timestamp: 将时间戳转化为日期
        @param format: 日期格式
        ---------
        @result: 返回日期
        """
        if timestamp is None:
            raise ValueError("timestamp is null")

        date = time.localtime(timestamp)
        return time.strftime(time_format, date)

    def get_sha1(self, *args):
        """
        @summary: 获取唯一的40位值， 用于获取唯一的id
        ---------
        @param *args: 参与联合去重的值
        ---------
        @result: ba4868b3f277c8e387b55d9e3d0be7c045cdd89e
        """

        sha1 = hashlib.sha1()
        for arg in args:
            sha1.update(str(arg).encode())
        return sha1.hexdigest()  # 40位

    def get_base64(self, data):
        if data is None:
            return data
        return base64.b64encode(str(data).encode()).decode("utf8")

    def get_uuid(self, key1="", key2=""):
        """
        @summary: 计算uuid值
        可用于将两个字符串组成唯一的值。如可将域名和新闻标题组成uuid，形成联合索引
        ---------
        @param key1:str
        @param key2:str
        ---------
        @result:
        """

        uuid_object = ""

        if not key1 and not key2:
            uuid_object = uuid.uuid1()
        else:
            hash = hashlib.md5(bytes(key1, "utf-8") + bytes(key2, "utf-8")).digest()
            uuid_object = uuid.UUID(bytes=hash[:16], version=3)

        return str(uuid_object)

    def get_random_password(self, length=8, special_characters=""):
        """
        @summary: 创建随机密码 默认长度为8，包含大写字母、小写字母、数字
        ---------
        @param length: 密码长度 默认8
        @param special_characters: 特殊字符
        ---------
        @result: 指定长度的密码
        """

        while True:
            random_password = "".join(
                random.sample(
                    string.ascii_letters + string.digits + special_characters, length
                )
            )
            if (
                    re.search("[0-9]", random_password)
                    and re.search("[A-Z]", random_password)
                    and re.search("[a-z]", random_password)
            ):
                if not special_characters:
                    break
                elif set(random_password).intersection(special_characters):
                    break

        return random_password

    def get_random_email(self, length=None, email_types: list = None, special_characters=""):
        """
        随机生成邮箱
        :param length: 邮箱长度
        :param email_types: 邮箱类型
        :param special_characters: 特殊字符
        :return:
        """
        if not length:
            length = random.randint(4, 12)
        if not email_types:
            email_types = [
                "qq.com",
                "163.com",
                "gmail.com",
                "yahoo.com",
                "hotmail.com",
                "yeah.net",
                "126.com",
                "139.com",
                "sohu.com",
            ]

        email_body = self.get_random_password(length, special_characters)
        email_type = random.choice(email_types)

        email = email_body + "@" + email_type
        return email