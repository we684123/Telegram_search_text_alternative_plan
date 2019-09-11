import json
import time
import pytz
import random
import telepot
import datetime
from telethon import TelegramClient, sync
from telethon import events, functions, types
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from telethon.tl.functions.messages import AddChatUserRequest
# 函式庫引入完畢

from config import base
base = base.base()
# 設定檔引入

owner = base['owner']
timezone = base['timezone']
bots_len = len(base['tgbots'])
group_name = base['group_name']
channel_id = base['channel_id']
interval_time = base['interval']
sleep_time = interval_time/bots_len
# 基本定義

bots = []
for i in range(len(base['tgbots'])):
    bots.append(telepot.Bot(base['tgbots'][0]['token']))
# tgbot準備完畢

api_id = int(base['userbot']['api_id'])
api_hash = base['userbot']['api_hash']
client = TelegramClient('prototype', api_id, api_hash)
client.start()
# userbot準備完畢


def sendMSG(bot, chat_id=None, ct=None, reply_to_message_id=None):
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

    bot.sendMessage(
        chat_id,
        text=t,
        parse_mode=parse_mode,
        disable_web_page_preview=disable_web_page_preview,
        disable_notification=disable_notification,
        reply_to_message_id=reply_to_message_id,
        reply_markup=reply_markup
    )


def rtc(text):
    if type(text) == str:
        return text.replace(
        '', ' ').replace('_', '\_').replace('*', '\*').replace('`', '\`')
    return ''
# ==================== 以上function準備 ==================== #


for dialog in client.get_dialogs(limit=10):
    print(dialog.name, dialog.draft.text)

group = client.get_entity(group_name)
central = pytz.timezone(timezone)
msg_link_head = 'https://t.me/c/{0}/'.format(group.id)
# for message in client.iter_messages(group, reverse=True):
# for message in client.iter_messages(group, limit=10, offset_id=100, reverse=True):
offset_id = int(input('plz input offset_id :\n'))
now_use = 0
now_time = time.time()
for message in client.iter_messages(group, limit=30, offset_id=offset_id, reverse=True):
    if message.text:
        now_use += 1
        entity = client.get_entity(PeerUser(message.from_id))
        print(now_use)
        print(message.id, message.from_id, rtc(message.text))
        #print(message)
        #print(entity)

        if type(entity) == 'coroutine':
            entity_deleted = True
            entity_first_name = '已刪除的帳號'
            entity_last_name = ''
        else:
            entity_first_name = entity.first_name
            entity_last_name = entity.last_name

        if entity_first_name == None:
            entity_first_name = '已刪除的帳號'
        if entity_last_name == None:
            entity_last_name = ''
        if message.media:
            endtxt = '[影片or照片]\n' + rtc(message.text)
        else:
            endtxt = rtc(message.text)

        txt = "{0}\n\nFN={2} LN={3}\nUID={1}   MID={6} \n [{4}]({5}) ".format(
            endtxt,
            message.from_id,
            entity_first_name,
            entity_last_name,
            str(message.date.astimezone(central)) + ' <-對話連結',
            (msg_link_head + str(message.id)),
            str(message.id),
        )
        st = {
            "type": "to_Telegram",
            "text": txt,
            "notification": False,
            "parse_mode": "Markdown"
        }
        # print(txt)
        target = now_use % bots_len
        sendMSG(bots[target], channel_id, st)
        print(base['tgbots'][target]['name'])
        interval_time = time.time() - now_time
        print('間隔 {0} 秒'.format(interval_time))
        print("========")

        time.sleep(sleep_time)
        #client.send_message(channel_id, txt)

    '''
    if message.id % 991 == 0:
        print('time.sleep(61)')
        time.sleep(61)
    if message.id % 307 == 0:
        print('time.sleep(5)')
        time.sleep(5)
    if message.id % 127 == 0:
        print('time.sleep(2)')
        time.sleep(2)
    '''
