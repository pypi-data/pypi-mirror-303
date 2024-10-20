"""
class163/playlist.py
Version: 0.7.5
Author: CooooldWind_
E-Mail: 3091868003@qq.com
Copyright @CooooldWind_ / Following GNU_AGPLV3+ License
"""

import time
from netease_encode_api import EncodeSession
from class163.music import BasicMusicType, Music
from urllib.parse import urlparse, parse_qs
from class163.global_args import *
from class163.common import extract, extract_in_list
from typing import Optional, Dict, List, Union, Type


class BasicPlaylistType:
    def __init__(self):
        self.title = None
        self.creator = None
        self.create_time = None
        self.last_update_time = None
        self.description = None
        self.track_count = None
        self.track: List[Union[Music, BasicMusicType, None]] = []

    def info_dict(self) -> Optional[Dict]:
        track_result = [basic_music.info_dict() for basic_music in self.track]
        result = {
            "title": self.title,
            "creator": self.creator,
            "create_time": self.create_time,
            "last_update_time": self.last_update_time,
            "description": self.description,
            "track_count": self.track_count,
            "track_info": track_result,
        }
        return result

class Playlist(BasicPlaylistType):
    def __init__(self, id: int | str) -> None:
        super().__init__()
        self.id = id
        if self.id.__class__ == str and self.id.find("music.163.com") != -1:
            self.id = url_to_id(self.id)
        self.encode_session = EncodeSession()  #  解码会话
        self.__encode_data = {
            "id": self.id,
        }

    def get_detail(self, each_music: bool = True, encode_session: EncodeSession = None) -> Optional[Dict]:
        if encode_session == None:
            encode_session = self.encode_session
        self.info_raw = encode_session.get_response(
            url="https://music.163.com/weapi/v6/playlist/detail",
            encode_data=self.__encode_data,
        )["playlist"]
        origin = self.info_raw
        result = self.extract_detail(origin=origin)
        if each_music:
            get_detail_list = []
            get_detail_index_list: list[int] = []
            for index in range(len(self.track)):
                self.track[index].update_encode_data()
                if self.track[index].title == None:
                    get_detail_list.append({"id":self.track[index].id})
                    get_detail_index_list.append(index)
                if len(get_detail_list) >= 30:
                    detail_encode_data = {
                        "c": str(get_detail_list),
                    }
                    detail_info_raw = encode_session.get_response(
                        url=DETAIL_URL,
                        encode_data=detail_encode_data,
                    )["songs"]
                    for now in range(len(get_detail_index_list)):
                        self.track[get_detail_index_list[now]].detail_info_raw = detail_info_raw[now]
                        self.track[get_detail_index_list[now]].extract_detail(origin=detail_info_raw[now])
                        self.track[get_detail_index_list[now]].update_encode_data()
                    get_detail_list.clear()
                    get_detail_index_list.clear()

                    
        result = self.info_dict()
        return result

    def extract_detail(
        self,
        origin: Dict,
        id_keys: List[Union[str, int]] = ["id"],
        title_keys: List[Union[str, int]] = ["name"],
        creator_keys: List[Union[str, int]] = ["creator", "nickname"],
        create_time_keys: List[Union[str, int]] = ["createTime"],
        last_update_time_keys: List[Union[str, int]] = ["updateTime"],
        description_keys: List[Union[str, int]] = ["description"],
        track_count_keys: List[Union[str, int]] = ["trackCount"],
        track_id_list_keys: List[Union[str, int]] = ["trackIds"],
        track_id_keys: List[Union[str, int]] = ["id"],
        track_list_keys: List[Union[str, int]] = ["tracks"],
    ) -> Optional[Dict]:
        self.id = extract(origin, id_keys, int)
        self.title = extract(origin, title_keys, str)
        self.creator = extract(origin, creator_keys, str)
        create_time_extract = extract(origin, create_time_keys, int)
        if create_time_extract is not None:
            create_time = time.localtime(int(create_time_extract) / 1000)
            self.create_time = list(create_time[0:5])
        last_update_time_extract = extract(origin, last_update_time_keys, int)
        if last_update_time_extract is not None:
            last_update_time = time.localtime(int(last_update_time_extract) / 1000)
            self.last_update_time = list(last_update_time[0:5])
        self.description = extract(origin, description_keys, str)
        self.track_count = extract(origin, track_count_keys, int)
        try:
            track_id_list = extract_in_list(
                extract(origin, track_id_list_keys, list), track_id_keys, int
            )
            for id in track_id_list:
                self.track.append(Music(id))
            track_list = extract(origin, track_list_keys, list)
            for index in range(len(track_list)):
                appending_music = Music(0)
                appending_music.detail_info_raw = track_list[index]
                appending_music.extract_detail(origin=appending_music.detail_info_raw)
                self.track[index] = appending_music
        except: pass
        return self.info_dict()
    
    def update_encode_data(self) -> None:
        self.__encode_data = {
            "id": self.id,
        }


def url_to_id(url: str) -> int:
    try:
        # 手动分割URL，获取hash部分
        if url.find("#/") != -1:
            hash_fragment = url.split("#")[1]
        else:
            hash_fragment = url
        # 解析hash部分的查询参数
        query_params = parse_qs(hash_fragment.split("?")[1])

        # 提取ID并转换为整数
        playlist_id = int(query_params.get("id", [None])[0])
        return playlist_id
    except (IndexError, ValueError, TypeError):
        raise ValueError("URL 中未找到 'id' 参数")


def playlist_from_detail(detail_dict: Dict) -> Playlist:
    result = Playlist(0)
    result.info_raw = detail_dict
    result.extract_detail(detail_dict)
    result.update_encode_data()
    return result
