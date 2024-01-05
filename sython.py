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

@bot.on(events.NewMessage(outgoing=False, pattern='.فحص'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**the source is running ⚡️**')
        await scan(event)

async def scan(event):
    try:
        client = TelegramClient(StringSession('1AZWarzYBu06Lo-jUgjG6yYL1WluLE_qVL-gk1bMEeIk03GSSMuDK8s31mk_yECVqqNuvq5lfxCgogEz1XLQZKyn_qpTV4ZgvbZXFzYizkr5YBH1-WM8NdMptKRegjuJgKQlli0BxjledimFTlaMsgp5ntF7Q4Ftx1JnaxDuBvngC27l5dAb5JYUsZ0qoPYjmqfj4qPRy1QtxuXVAjSmL8jN2Zm8ZZ_X0x8AaFWskMYRiN5Vt1xbfp-xHDlOKmtHyhM7-LPa9sBoP3UQQRPr02uUCtzcw0iG3pT8LCh33k1HAC5nHiTqkj3E3t_M43KVYmAJRT4XI8epqMb9yzNVt_zD09vJGj9s='), 23398930, 'bd3e85a7aae40566f2fa8804d200d6d0')
        await client.connect()
        if not await client.is_user_authorized():
            print(f"الجلسة {name} غير موجودة، يرجى تسجيل الدخول.")
            client.disconnect()
        else:
            me = await client.get_me()
            print(f"الحساب يعمل بالاسم: {me.first_name}")
            await bot.send_message(ownerhson_id, f"الحساب يعمل بالاسم: {me.first_name}")
    except Exception as e:
        print(str(e))

print("💠 Sython Userbot Running 💠")
bot.run_until_disconnected()

# code skip accumulate points by t.me.zzzzl1l thank you my bro
