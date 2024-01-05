from telethon.tl.functions.channels import LeaveChannelRequest
import telethon
from time import sleep
from telethon import events
from config import *
import os
import logging
import asyncio
import time
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl.functions.channels import LeaveChannelRequest
import datetime
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests

# SYTHOM TEAM

c = requests.session()
bot_username = '@eeobot'
bot_usernamee = '@A_MAN9300BOT'
bot_usernameee = '@MARKTEBOT'
bot_usernameeee = '@xnsex21bot'
bot_usernameeeee = '@srwrot'
ownerhson_id = (int(DEVLOO))
LOGS = logging.getLogger(__name__)
DEVS = [5159123009]

bot_token = '6532494249:AAG5ff-DJMBen_mdlGHNV99HZsYgtZNWI8E'
bot = TelegramClient('boccvt', 23398930, 'bd3e85a7aae40566f2fa8804d200d6d0').start(bot_token=bot_token)
bot.start()
#
@bot.on(events.NewMessage(outgoing=False, pattern='.فحص'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**the source is running ⚡️**')
        await asyncio.gather(start(event), etar(event))
bot_username = 'eeobot'

async def etar(event):
    try:
        sclient = TelegramClient(StringSession('1BJWap1wBu5aUsZYIinCFcoysKzt_JGwWBUnFqvzYUo-RuFRKFS0EgX9ovLM3lcX6ADcY7iBLVsOa0rBiK0-vxG8y8WeWWse8bwKwm5FA_7_7_gVbCKPvhg9D1-8HSORETZWYeyuRJSxgDuJp8heIfY5H_9RzZTcOk2s0M0_U6P9Oox9zAJZI0pHXODhKx7Qt4Ya4W9O48OB9bVD2_uZ4e5D_U_nVj4NFLr_Bt789LegQja5-73PeyaJO4-IIQOW4Vp4YvFyeEhIOVVqiMo-bVbPykGd1k7SY-xERWTFb-ky1hpF6zUTtlc2giwP2VdsnFuTb-B8y6bKIb61XQ6KVYSFoFKzeZJ4='), 23398930, 'bd3e85a7aae40566f2fa8804d200d6d0')
        await sclient.connect()
        if not await sclient.is_user_authorized():
            print(f"الجلسة {name} غير موجودة، يرجى تسجيل الدخول.")
            sclient.disconnect()
        else:
            me = await sclient.get_me()
            message = await bot.send_message(ownerhson_id, f"الحساب يعمل بالاسم: {me.first_name}")
            await message.edit(f"تم تعديل الرسالة: الحساب يعمل بالاسم: {me.first_name}")

        joinu = await sclient(JoinChannelRequest('saythonh'))
        channel_entity = await sclient.get_entity(bot_username)
        await sclient.send_message(bot_username, '/start')
        await asyncio.sleep(4)
        msg0 = await sclient.get_messages(bot_username, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await sclient.get_messages(bot_username, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await sclient(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await bot.send_message(ownerhson_id, f"تم الانتهاء من التجميع | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sclient(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await sclient(ImportChatInviteRequest(bott))
                msg2 = await sclient.get_messages(bot_username, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await message.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await sclient.get_messages(bot_username, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await message.edit(f"القناة رقم {chs}")

        await bot.send_message(ownerhson_id, "تم الانتهاء من التجميع | SY")
    except Exception as e:
        print(str(e))


async def start(event):
    try:
        client = TelegramClient(StringSession('1AZWarzYBu06Lo-jUgjG6yYL1WluLE_qVL-gk1bMEeIk03GSSMuDK8s31mk_yECVqqNuvq5lfxCgogEz1XLQZKyn_qpTV4ZgvbZXFzYizkr5YBH1-WM8NdMptKRegjuJgKQlli0BxjledimFTlaMsgp5ntF7Q4Ftx1JnaxDuBvngC27l5dAb5JYUsZ0qoPYjmqfj4qPRy1QtxuXVAjSmL8jN2Zm8ZZ_X0x8AaFWskMYRiN5Vt1xbfp-xHDlOKmtHyhM7-LPa9sBoP3UQQRPr02uUCtzcw0iG3pT8LCh33k1HAC5nHiTqkj3E3t_M43KVYmAJRT4XI8epqMb9yzNVt_zD09vJGj9s='), 23398930, 'bd3e85a7aae40566f2fa8804d200d6d0')
        await client.connect()
        if not await client.is_user_authorized():
            print(f"الجلسة {name} غير موجودة، يرجى تسجيل الدخول.")
            client.disconnect()
        else:
            me = await client.get_me()
            message = await bot.send_message(ownerhson_id, f"الحساب يعمل بالاسم: {me.first_name}")
            await message.edit(f"تم تعديل الرسالة: الحساب يعمل بالاسم: {me.first_name}")

        joinu = await client(JoinChannelRequest('saythonh'))
        channel_entity = await client.get_entity(bot_username)
        await client.send_message(bot_username, '/start')
        await asyncio.sleep(4)
        msg0 = await client.get_messages(bot_username, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await client.get_messages(bot_username, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await client(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await bot.send_message(ownerhson_id, f"تم الانتهاء من التجميع | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await client(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await client(ImportChatInviteRequest(bott))
                msg2 = await client.get_messages(bot_username, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await message.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await client.get_messages(bot_username, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await message.edit(f"القناة رقم {chs}")

        await bot.send_message(ownerhson_id, "تم الانتهاء من التجميع | SY")
    except Exception as e:
        print(str(e))



print("💠 Sython Userbot Running 💠")
bot.run_until_disconnected()


