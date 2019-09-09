import json
import time
import pytz
import asyncio
import datetime
import telepot
import configparser
from pprint import pprint
import telethon.sync
from telethon import TelegramClient, sync
from telethon.tl.functions.messages import AddChatUserRequest
from telethon import events, functions, types
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
# 函式庫引入完畢

config = configparser.ConfigParser()
config.read('config.txt', encoding='utf8')
# config.txt準備完畢

bot_token = "978977382:AAHHe-PBTpwFmSNBMQciqVTXkbG8ZNmGihU"
bot = telepot.Bot(bot_token)
# bot準備完畢

api_id = int(config['token']['api_id'])
api_hash = config['token']['api_hash']
client = TelegramClient('Portalgram', api_id, api_hash)
client.start()
# userbot準備完畢


def sendMSG(chat_id=None, ct=None, reply_to_message_id=None):
    if chat_id == None:
        raise('chat_id loss')
    if ct == None:
        raise('ct loss')
    t = ct['text']
    if t == '':
        raise('text loss')
    if type(t) == list:
        test = ''
        for i in t:
            test += i
        t = test

    if 'parse_mode' in ct.keys():
        parse_mode = ct['parse_mode']
    else:
        parse_mode = None
    if 'disable_web_page_preview' in ct.keys():
        disable_web_page_preview = ct['disable_web_page_preview']
    else:
        disable_web_page_preview = None
    if 'disable_notification' in ct.keys():
        disable_notification = ct['disable_notification']
    else:
        disable_notification = None
    if 'reply_markup' in ct.keys():
        reply_markup = ct['reply_markup']
    else:
        reply_markup = None

    bot.sendMessage(chat_id, text=t, parse_mode=parse_mode,     disable_web_page_preview=disable_web_page_preview,
                    disable_notification=disable_notification, reply_to_message_id=reply_to_message_id,  reply_markup=reply_markup)


def rtc(text):
    if type(text) == str:
        return text.replace('', ' ')
    return ''
# ==================== 以上function準備 ==================== #


for dialog in client.get_dialogs(limit=10):
    print(dialog.name, dialog.draft.text)
group = await client.get_entity('修真•聊天•群')
channel_id = "-1001426948990"
central = pytz.timezone("Asia/Taipei")

for message in client.iter_messages(group, limit=200, reverse=True):
    if message.text:
        entity = client.get_entity(PeerUser(message.from_id))
        print(message.id, message.from_id, rtc(message.text))
        print(message)

        # print(entity.first_name)
        # print(entity.last_name)
        print(message.date.astimezone(central))
        print(entity)
        #print(entity.deleted)

        if type(entity) == 'coroutine':
            entity_deleted = True
            entity_first_name = '已刪除的帳號'
            entity_last_name = ''
        else:
            entity_first_name = entity.first_name
            entity_last_name = entity.last_name


        if entity_last_name == None:
            entity_last_name = ''

        txt = "{0}\n\nfirst_name={1} last_name={2}\nmessage_id={3} time={4} ".format(
            rtc(message.text),
            entity_first_name,
            entity_last_name,
            message.id,
            message.date.astimezone(central)
        )
        st = {
            "type": "to_Telegram",
            "text": txt,
            "notification": True,
            "parse_mode": ""
        }
        sendMSG(channel_id, st)
    else:
        st = {
            "type": "to_Telegram",
            "text": '[其他內容]',
            "notification": True,
            "parse_mode": "Markdown"
        }
        sendMSG(channel_id, st)

'''
print(entity)
type(entity)
print(entity.deleted)
'''

sendMSG(channel_id,{'type': 'to_Telegram',
 'text': ' o k 了 \n\nfirst_name=None last_name=\nmessage_id=2 time=2017-02-19 19:39:34+08:00 ',
 'notification': True,
 'parse_mode': ''})
