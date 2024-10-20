"""
class163/login.py
Version: 0.7.6
Author: CooooldWind_
E-Mail: 3091868003@qq.com
Copyright @CooooldWind_ / Following GNU_AGPLV3+ License
"""

from netease_encode_api import EncodeSession
from typing import Dict
from class163.global_args import *


class Login:
    def __init__(self) -> str:
        self.encode_session = EncodeSession()
        self.__encode_data = {"type": "1"}
        self.unikey: str = self.encode_session.get_response(
            url=LOGIN_URL, encode_data=self.__encode_data
        )["unikey"]
        self.__check_encode_data = {"key": self.unikey, "type": "1"}
        self.login_link = (
            f"https://music.163.com/login?codekey={self.unikey}&refer=scan"
        )
        return self.login_link

    def check_status(self) -> Dict:
        origin = self.encode_session.get_response(
            url=LOGIN_CHECK_URL, encode_data=self.__check_encode_data
        )
        login_code = int(origin["code"])
        if login_code == 800:
            return {"status": "failed"}
        elif login_code == 801:
            return {"status": "wait"}
        elif login_code == 802:
            return {"status": "login", "user": origin["nickname"]}
        elif login_code == 803:
            return{"status": "succeed", "session": self.encode_session}



"""
from selenium import webdriver

def login() -> dict:
    driver = webdriver.ChromiumEdge()
    driver.get("https://music.163.com/#/login/")
    cookies = None
    while cookies == None:
        cookies = driver.get_cookie("MUSIC_U")
        if cookies != None:
            cookies = {cookies["name"]: cookies["value"]}
            driver.close()
            break
    return cookies
"""
