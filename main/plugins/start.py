#Github.com/Vasusen-code

import os
from .. import bot as Drone
from telethon import events, Button

from telethon import events, Button


async def start_srb(event, st):
    await event.reply(st, 
                      buttons=[
                              [Button.inline("SET THUMB.", data="set"),
                               Button.inline("REM THUMB.", data="rem")],
                              [Button.url("DEV", url="https://t.me/Bot_update_i")]])
                              
    
async def vc_menu(event):
    await event.edit("**VIDEO CONVERTOR v1.4**", 
                    buttons=[
                        [Button.inline("info.", data="info")],
                        [Button.inline("Main.", data="help")],
                        [Button.url("DEVELOPER", url="https://t.me/Soonbotmaker0")]])
    
S = '/' + 's' + 't' + 'a' + 'r' + 't'

@Drone.on(events.callbackquery.CallbackQuery(data="set"))
async def sett(event):    
    Drone = event.client                    
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    async with Drone.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("Send me any image for thumbnail as a `reply` to this message.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("No media found.")
        mime = x.file.mime_type
        if not 'png' in mime:
            if not 'jpg' in mime:
                if not 'jpeg' in mime:
                    return await xx.edit("No image found.")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'Trying.')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("Temporary thumbnail saved!")
        
@Drone.on(events.callbackquery.CallbackQuery(data="rem"))
async def remt(event):  
    Drone = event.client            
    await event.edit('Trying.')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('Removed!')
    except Exception:
        await event.edit("No thumbnail saved.")                        
  
@Drone.on(events.NewMessage(incoming=True, pattern=f"{S}"))
async def start(event):
    text = "Send me Link of any message to clone it here, For private channel message, send invite link first.\n\n**SUPPORT:** @Bot_update_i"
    await start_srb(event, text)
    
