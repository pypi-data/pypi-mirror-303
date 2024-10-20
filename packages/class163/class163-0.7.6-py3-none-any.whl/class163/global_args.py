"""
class163/music.py
Version: 0.7.6
Author: CooooldWind_
E-Mail: 3091868003@qq.com
Copyright @CooooldWind_ / Following GNU_AGPLV3+ License
"""

from typing import Literal
from typing_extensions import TypeAlias


FILE_URL = "https://music.163.com/weapi/song/enhance/player/url/v1"
LYRIC_URL = "https://music.163.com/weapi/song/lyric"
DETAIL_URL = "https://music.163.com/weapi/v3/song/detail"
SEARCH_URL = "https://music.163.com/weapi/cloudsearch/get/web"
LOGIN_URL = "https://music.163.com/weapi/login/qrcode/unikey"
LOGIN_CHECK_URL = "https://music.163.com/weapi/login/qrcode/client/login"
LEVEL: TypeAlias = Literal["standard", "higher", "exhigh", "lossless"]
MODE: TypeAlias = Literal[
    "d",
    "l",
    "f",
    "df",
    "dl",
    "fd",
    "fl",
    "ld",
    "lf",
    "fld",
    "fdl",
    "ldf",
    "lfd",
    "dfl",
    "dlf",
]
MUSIC_FILE_TYPE: TypeAlias = Literal["mp3", "flac"]
SEARCH_TYPE: TypeAlias = Literal["song", "artist", "playlist", "album"]
