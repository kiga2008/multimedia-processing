""" This module defines the constants or default values.
"""
from pydantic import BaseModel, validator
from watermark import Position


class Config(BaseModel):
    watermark: str = "https://raw.githubusercontent.com/kiga2008/watermarkbot/main/ruya.png"
    frame_rate: int = 15
    preset: str = "ultrafast"
    position: Position = Position.centre

    @validator("preset")
    def validate_preset(val):
        allowed = ["ultrafast", "fast", "medium", "slow"]
        if not val in allowed:
            raise ValueError(f"Choose preset from {allowed}")
        return val


START = """正在工作中!"""

HELP = """
使用方法很简单，只需要发送一张图片、视频、gif，机器人会自动打好水印并返回。

机器人命令： `/set` 与 `/get` 可以设置与获取当前的配置。 

SET语法为： `/set` ➜  `/set key: value`
GET语法为： `/get` ➜  `/get key`

"""

COMMANDS = {
    "start": "尝试启动BOT，查看是否在工作中",
    "get": "获取当前配置",
    "setWM1": "西安儒雅群，t.me/xianruya",
    "setWM2": "https://t.me/xianruya",
    "setWM3": "@xianruya",
    "setWM4": "@xahades http://t.me/xaHades",
    "setWM5": "@PreHades",
    "set": "通过SET命令设置配置",
    "help": "使用帮助",
}

config = Config()
