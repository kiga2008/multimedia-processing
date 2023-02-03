""" This module defines the functions that handle different events.
"""
import os
from telethon import events
from watermark import File, Watermark, apply_watermark

from telewater import conf
from telewater.utils import cleanup, download_image, gen_kv_str, get_args, stamp
import subprocess

async def start(event):
    await event.respond(conf.START)
    raise events.StopPropagation

async def set_wm1(event):
    await event.respond(conf.SETWM1)
    conf.config.curWM = "西安儒雅群 t.me/xianruya"
    raise events.StopPropagation
    
async def set_wm2(event):
    await event.respond(conf.SETWM2)
    conf.config.curWM = "t.me/xianruya"
    raise events.StopPropagation
   
async def set_wm3(event):
    await event.respond(conf.SETWM3)
    conf.config.curWM = "@xianruya"
    raise events.StopPropagation
    
async def set_wm4(event):
    await event.respond(conf.SETWM4)
    conf.config.curWM = "@xahades t.me/XaHades"
    raise events.StopPropagation
    
async def set_wm5(event):
    await event.respond(conf.SETWM5)
    conf.config.curWM = "@PreHades"
    raise events.StopPropagation
    
async def bot_help(event):
    try:
        await event.respond(conf.HELP)
    finally:
        raise events.StopPropagation


async def set_config(event):

    notes = f"""这条SET命令是用来设置配置的
    使用： `/set key: val`
    例子： `/set watermark: https://link/to/watermark.png`
    {gen_kv_str()}
    """.replace(
        "    ", ""
    )

    try:
        pos_arg = get_args(event.message.text)
        if not pos_arg:
            raise ValueError(f"{notes}")
        splitted = pos_arg.split(":", 1)

        if not len(splitted) == 2:
            raise ValueError("错误的配置格式")

        key, value = [item.strip() for item in splitted]

        config_dict = conf.config.dict()
        if not key in config_dict.keys():
            raise ValueError(f"KEY： {key} 错误，请重新检查")

        config_dict[key] = value
        print(config_dict)

        conf.config = conf.Config(**config_dict)

        print(conf.config)
        
        if key == "watermark":
            if value == "1":
                download_image(url="https://raw.githubusercontent.com/kiga2008/watermarkbot/main/ruya.png",filename="ruya.png")
            elif value == "2":
                download_image(url="https://raw.githubusercontent.com/kiga2008/watermarkbot/main/@httpxianruya.png",filename="@httpxianruya.png")
            elif value == "3":
                download_image(url="https://raw.githubusercontent.com/kiga2008/watermarkbot/main/@xianruya.png",filename="@xianruya.png")
            elif value == "4":
                download_image(url="https://raw.githubusercontent.com/kiga2008/watermarkbot/main/@xahades.png",filename="@xahades.png")
            elif value == "5":
                download_image(url="https://raw.githubusercontent.com/kiga2008/watermarkbot/main/@prehades.png",filename="@prehades.png")
        await event.respond(f"KEY： {key} ，设置成功")
        

    except ValueError as err:
        print(err)
        await event.respond(str(err))
    except Exception as err:
        print(err)

    finally:
        raise events.StopPropagation


async def get_config(event):

    notes = f"""这条GET命令是用来获取配置的
    使用： `/get key`
    例子： `/get x_off`
    {gen_kv_str()}
    """.replace(
        "    ", ""
    )

    try:
        key = get_args(event.message.text)
        if not key:
            raise ValueError(f"{notes}")
        config_dict = conf.config.dict()
        await event.respond(f"{config_dict.get(key)}")
    except ValueError as err:
        print(err)
        await event.respond(str(err))

    finally:

        raise events.StopPropagation

async def watermarker(event):

    if not (event.gif or event.photo or event.video or event.text):
        await event.respond("文件格式不支持")
        return

    if(event.text):
        conf.config.curWM = event.text
        await event.respond("成功设置新文字水印！")
    else:
        org_file = stamp(await event.download_media(""), user=str(event.sender_id))

        file = File(org_file)

        out_file = apply_wm(
            file,wtm=conf.config.curWM, frame_rate=conf.config.frame_rate, preset=conf.config.preset
        )
        await event.client.send_file(event.sender_id, out_file)
        cleanup(org_file, out_file)

    
"""TRY WM BEGIN"""
def apply_wm(
    file: File,
    wtm: "西安儒雅群",
    output_file: str = "",
    frame_rate: int = 15,
    preset: str = "ultrafast",
) -> str:

    if not output_file:
        output_file = f"watered_{file.path}"
        
    cmd = [
        "ffmpeg",
        "-i",
        file.path,
        "-f",
        "lavfi",
        "-i",
        f"color=white@0:s=300*300,format=yuva420p",
        "-filter_complex",
        f"[1]trim=end_frame=1,drawtext=font='MoeStandardKai.ttf':text={wtm}:fontcolor=white:fontsize=24:x=0:y=150:alpha=0.9,rotate=a=30*PI/180:c=black@0,loop=-1:1:0,tile=15x15,trim=end_frame=1[wm];[0][wm]overlay=0:0",
        "-c:a",
        "copy",
        "-preset",
        "encoding_preset",
        output_file,
    ]

    if os.path.isfile(output_file) and overwrite:
        os.remove(output_file)

    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return output_file
"""TRY WM BEGIN"""
ALL_EVENTS = {
    "start": (start, events.NewMessage(pattern="/start")),
    "get": (get_config, events.NewMessage(pattern="/get")),
    "watermark1": (set_wm1, events.NewMessage(pattern="/watermark1")),
    "watermark2": (set_wm2, events.NewMessage(pattern="/watermark2")),
    "watermark3": (set_wm3, events.NewMessage(pattern="/watermark3")),
    "watermark4": (set_wm4, events.NewMessage(pattern="/watermark4")),
    "watermark5": (set_wm5, events.NewMessage(pattern="/watermark5")),
    "help": (bot_help, events.NewMessage(pattern="/help")),
    "set": (set_config, events.NewMessage(pattern="/set")),
    "watermarker": (watermarker, events.NewMessage()),
}
# this is a dictionary where the keys are the unique string identifier for the events
# the values are a tuple consisting of callback function and event
