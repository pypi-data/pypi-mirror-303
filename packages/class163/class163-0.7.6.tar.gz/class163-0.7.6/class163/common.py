"""
class163/common.py
Version: 0.6.9
Author: CooooldWind_/马建仓AI助手@Gitee/豆包@字节跳动
E-Mail: 3091868003@qq.com
Copyright @CooooldWind_ / Following GNU_AGPLV3+ License
"""

import io
from typing import Optional, Dict, List, Union, Type
from PIL import Image
from mutagen.id3 import ID3, TALB, TPE1, TIT2, APIC
from class163.global_args import MUSIC_FILE_TYPE


def extract(origin: Dict, keys: List[Union[str, int]], expected_type: Type):
    """
    从字典中提取信息。

    :param origin: 源字典
    :param keys: 键列表
    :param expected_type: 期望的类型
    :return: 提取的结果，如果失败则返回 None
    """
    try:
        temp_dict = origin
        for key in keys:
            temp_dict = temp_dict[key]
        return temp_dict if isinstance(temp_dict, expected_type) else None
    except (KeyError, TypeError, IndexError):
        return None


def extract_in_list(
    origin: List[Optional[Dict]],
    keys: List[Union[str, int]],
    expected_type: Type,
) -> List:
    """
    在字典列表中提取信息。

    :param origin: 源字典列表
    :param keys: 键列表
    :param expected_type: 期望的类型
    :return: 提取结果的列表
    """
    return [extract(item, keys, expected_type) for item in origin]


def artist_join(artist: list[str], separator: str = ", ") -> str:
    """
    将歌手列表连接为一个字符串。
    :param artist: 歌手列表。
    :param separator: 分隔符，默认为", "。
    :return: 连接后的字符串。
    """
    """
    artist_str = ""
    for i in artist[:-1]:
        artist_str += i + separator
    artist_str += artist[-1]
    return artist_str
    """
    return separator.join(artist)


def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred in function {func.__name__}: {e}")
            return None

    return wrapper


@error_handler
def attribute_write_mp3(file: bytes, attribute: Dict) -> bytes:
    file_obj = io.BytesIO(file)
    id3_file_obj = ID3()
    id3_file_obj.load(file_obj)
    id3_file_obj["TALB"] = TALB(encoding=3, text=[attribute["album"]])
    id3_file_obj["TPE1"] = TPE1(encoding=3, text=artist_join(attribute["artist"], "; "))
    id3_file_obj["TIT2"] = TIT2(encoding=3, text=[attribute["title"]])
    id3_file_obj.save(file_obj, v2_version=3)
    return file_obj.getvalue()


@error_handler
def cover_write_mp3(file: bytes, cover: bytes) -> bytes:
    file_obj = io.BytesIO(file)
    id3_file_obj = ID3()
    id3_file_obj.load(file_obj)
    # cover_file_obj = Image.open(cover)
    # cover_data = cover_file_obj.tobytes()
    id3_file_obj.add(
        APIC(encoding=3, mime="image/jpeg", type=3, desc="Cover", data=cover)
    )
    id3_file_obj.save(file_obj, v2_version=3)
    return file_obj.getvalue()

def clean(filename: str) -> str:
    """
    清空有悖于标准的字符的函数。
    ----------
    参数：
    1. `filename`: 文件名
    """
    filename_return = filename
    dirty = [":", "*", '"', "?", "|", "<", ">", "/", "\\"]
    for i in dirty:
        filename_return = filename_return.replace(i, "_")
    return filename_return