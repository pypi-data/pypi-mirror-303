"""
class163/music.py
Version: 0.7.6
Author: CooooldWind_/豆包@字节跳动
E-Mail: 3091868003@qq.com
Copyright @CooooldWind_ / Following GNU_AGPLV3+ License
"""

from netease_encode_api import EncodeSession
from class163.global_args import *
from class163.common import extract
from class163.music import Music, music_from_detail
from class163.playlist import Playlist, playlist_from_detail
from typing import Optional, Dict, List, Union


class Search:
    def __init__(
        self,
        key: str,
        cookie_dict: Optional[Dict] = None,
        search_type: SEARCH_TYPE = "song",
        encode_session: Optional[EncodeSession] = None,
    ):
        if encode_session != None:
            self.encode_session = encode_session
        else:
            self.encode_session = EncodeSession()
            if cookie_dict != None:
                self.encode_session.set_cookies(cookie_dict)
            else:
                raise Exception("Need cookie_dict or encode_session.")
        self.search_type = search_type
        encode_type = ""
        if self.search_type == "song":
            encode_type = "1"
        elif self.search_type == "album":
            encode_type = "10"
        elif self.search_type == "artist":
            encode_type = "100"
        elif self.search_type == "playlist":
            encode_type = "1000"
        self.result_count = 0
        self.__encode_data = {
            "s": key,
            "type": encode_type,  # 歌曲-1 专辑-10 歌手-100 歌单-1000
            "offset": "0",
            "total": "true",
            "limit": "65536",
        }
        self.search_result_raw = {}
        self.search_result_sorted: list[Union[Music, Playlist, None]] = []

    def get(
        self, encode_session: EncodeSession = None
    ) -> Union[List, Dict, None]:
        if encode_session is None:
            encode_session = self.encode_session
        # 这需要有 cookies 才能使用
        if "MUSIC_U" not in dict(self.encode_session.session.cookies.get_dict()).keys():
            return None
        # 第一次搜索结果
        origin = encode_session.get_response(
            url=SEARCH_URL, encode_data=self.__encode_data
        )["result"]
        self.result_count = extract(origin, [f"{self.search_type}Count"], int)
        self.search_result_raw = origin
        # 如果有歌曲就加进去
        if self.search_type == "song":
            for i in self.search_result_raw["songs"]:
                self.search_result_sorted.append(music_from_detail(i))
            return self.search_result_sorted
        elif self.search_type == "playlist":
            for i in self.search_result_raw["playlists"]:
                self.search_result_sorted.append(playlist_from_detail(i))
            return self.search_result_sorted
        return self.search_result_raw
