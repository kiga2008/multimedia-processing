""" This module defines the constants or default values.
"""
from pydantic import BaseModel, validator
from watermark import Position


class Config(BaseModel):
    watermark: str = "https://raw.githubusercontent.com/kiga2008/watermarkbot/main/ruya.png"
    frame_rate: int = 15
    preset: str = "ultrafast"
    position: Position = Position.centre
    curWM : str = "image.png"
<<<<<<< HEAD
    color : str = "black"
    alpha : int = 1
=======
>>>>>>> main

    @validator("preset")
    def validate_preset(val):
        allowed = ["ultrafast", "fast", "medium", "slow"]
        if not val in allowed:
            raise ValueError(f"Choose preset from {allowed}")
        return val

START = """正在工作中!"""

""" 步骤4，改说明即可
"""
SETWM1 = """图片水印为『西安儒雅群』"""
SETWM2 = """图片水印为『哈迪斯の后花园』"""
SETWM3 = """图片水印为『海纳百川』"""
SETWM4 = """全屏文字水印为『西安儒雅群t.me/xianruya』"""
SETWM5 = """全屏文字水印为『@xahades http://t.me/xaHades』"""
SETWM6 = """全屏文字水印为『海纳百川 @hnbcshare』"""

HELP = """
使用方法很简单，只需要发送一张图片、视频、gif，机器人会自动打好水印并返回。

机器人命令： `/set` 与 `/get` 可以设置与获取当前的配置。 

SET语法为： `/set` ➜  `/set key: value`
GET语法为： `/get` ➜  `/get key`

"""

<<<<<<< HEAD
""" 步骤5，改说明即可
"""
COMMANDS = {
    "start": "尝试启动BOT，查看是否在工作中",
    "get": "获取当前配置",
    "watermark1" : "大水印：西安儒雅群",
    "watermark2" : "大水印：哈迪斯の后花园",
    "watermark3" : "大水印：海纳百川",
    "watermark4" : "全屏文字：西安儒雅群t.me/xianruya",
    "watermark5" : "全屏文字：@XaHades t.me/xaHades",
    "watermark6" : "全屏文字：海纳百川 @hnbcshare",
    "set": "设置当前配置",
=======
SETWM1 = """成功设置水印为『西安儒雅群，t.me/xianruya』"""
SETWM2 = """成功设置水印为『https://t.me/xianruya』"""
SETWM3 = """成功设置水印为『@xianruya』"""
SETWM4 = """成功设置水印为『@xahades http://t.me/xaHades』"""
SETWM5  = """成功设置水印为『@PreHades』"""

COMMANDS = {
    "start": "尝试启动BOT，查看是否在工作中",
    "get": "获取当前配置",
    "set wm 1" : "西安儒雅群，t.me/xianruya",
    "set wm 2" : "https://t.me/xianruya",
    "set wm 3" : "@xianruya",
    "set wm 4" : "@xahades http://t.me/xaHades",
    "set wm 5" : "@PreHades",
    "set": "通过SET命令设置配置",
>>>>>>> main
    "help": "使用帮助",
}

config = Config()
