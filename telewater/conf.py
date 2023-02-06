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
    color : str = "black"
    alpha : int = 1

    @validator("preset")
    def validate_preset(val):
        allowed = ["ultrafast", "fast", "medium", "slow"]
        if not val in allowed:
            raise ValueError(f"Choose preset from {allowed}")
        return val


START = """正在工作中!"""

SETWM1 = """图片水印为『西安儒雅群』"""
SETWM2 = """图片水印为『哈迪斯の后花园』"""
SETWM3 = """全屏文字水印为『西安儒雅群t.me/xianruya』"""
SETWM4 = """全屏文字水印为『@xahades http://t.me/xaHades』"""

HELP = """
使用方法很简单，只需要发送一张图片、视频、gif，机器人会自动打好水印并返回。

机器人命令： `/set` 与 `/get` 可以设置与获取当前的配置。 

SET语法为： `/set` ➜  `/set key: value`
GET语法为： `/get` ➜  `/get key`

"""

COMMANDS = {
    "start": "尝试启动BOT，查看是否在工作中",
    "get": "获取当前配置",
    "watermark1" : "大水印：西安儒雅群",
    "watermark2" : "大水印：哈迪斯の后花园",
    "watermark3" : "全屏文字：西安儒雅群t.me/xianruya",
    "watermark4" : "全屏文字：@XaHades t.me/xaHades",
    "set": "设置当前配置",
    "help": "使用帮助",
}

config = Config()
