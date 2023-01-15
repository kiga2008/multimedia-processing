""" This module defines the functions that handle different events.
"""

from telethon import events
from watermark import File, Watermark, apply_watermark

from telewater import conf
from telewater.utils import cleanup, download_image, gen_kv_str, get_args, stamp


async def start(event):
    await event.respond(conf.START)
    raise events.StopPropagation


async def bot_help(event):
    try:
        await event.respond(conf.HELP)
    finally:
        raise events.StopPropagation

async def setwm1(event):
    await event.respond(conf.SETWM1)
    config.curWM = "ruya.png"
    raise events.StopPropagation
    
async def setwm2(event):
    await event.respond(conf.SETWM2)
    config.curWM = "@httpxianruya.png"
    raise events.StopPropagation
    
async def setwm3(event):
    await event.respond(conf.SETWM3)
    config.curWM = "@xianruya.png"
    raise events.StopPropagation
    
async def setwm4(event):
    await event.respond(conf.SETWM4)
    config.curWM = "@xahades.png"
    raise events.StopPropagation
    
async def setwm5(event):
    await event.respond(conf.SETWM5)
    config.curWM = "@prehades.png"
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
        if key == "watermark" and value == "1":
            cleanup("image.png")
            download_image(url="https://raw.githubusercontent.com/kiga2008/watermarkbot/main/ruya.png",filename="ruya.png")
        await event.respond(f"KEY： {key} ，成功被设置成： {"西安儒雅群 t.me\/xianruya"}")

        if key == "watermark" and value == "2":
            cleanup("image.png")
            download_image(url="https://raw.githubusercontent.com/kiga2008/watermarkbot/main/@httpxianruya.png",filename="@httpxianruya.png")
        await event.respond(f"KEY： {key} ，成功被设置成： {"https:\/\/t.me\/xianruya"}")
        
        if key == "watermark" and value == "3":
            cleanup("image.png")
            download_image(url="https://raw.githubusercontent.com/kiga2008/watermarkbot/main/@xianruya.png",filename="@xianruya.png")
        await event.respond(f"KEY： {key} ，成功被设置成： {"@xianruya"}")
        
        if key == "watermark" and value == "4":
            cleanup("image.png")
            download_image(url="https://raw.githubusercontent.com/kiga2008/watermarkbot/main/@xahades.png",filename="@xahades.png")
        await event.respond(f"KEY： {key} ，成功被设置成： {"@xahades http:\/\/t.me\/xaHades"}")
        
        if key == "watermark" and value == "5":
            cleanup("image.png")
            download_image(url="https://raw.githubusercontent.com/kiga2008/watermarkbot/main/@prehades.png",filename="@prehades.png")
        await event.respond(f"KEY： {key} ，成功被设置成： {"@PreHades"}")
        
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

    if not (event.gif or event.photo or event.video):
        await event.respond("文件格式不支持")
        return

    org_file = stamp(await event.download_media(""), user=str(event.sender_id))

    file = File(org_file)
    wtm = Watermark(File(config.curWM), pos=conf.config.position)

    out_file = apply_watermark(
        file, wtm, frame_rate=conf.config.frame_rate, preset=conf.config.preset
    )
    await event.client.send_file(event.sender_id, out_file)
    cleanup(org_file, out_file)


ALL_EVENTS = {
    "start": (start, events.NewMessage(pattern="/start")),
    "get": (get_config, events.NewMessage(pattern="/get")),
    "setwm1" : (set_wm1, events.NewMessage(pattern="/setwm1")),
    "setwm2" : (set_wm2, events.NewMessage(pattern="/setwm2")),
    "setwm3" : (set_wm3, events.NewMessage(pattern="/setwm3")),
    "setwm4" : (set_wm4, events.NewMessage(pattern="/setwm4")),
    "setwm5" : (set_wm5, events.NewMessage(pattern="/setwm5")),
    "help": (bot_help, events.NewMessage(pattern="/help")),
    "set": (set_config, events.NewMessage(pattern="/set")),
    "watermarker": (watermarker, events.NewMessage()),
}
# this is a dictionary where the keys are the unique string identifier for the events
# the values are a tuple consisting of callback function and event
