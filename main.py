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
from ckiptagger import data_utils, construct_dictionary, WS
# 函式庫引入完畢

from config import base
from config import weights_dictionary
base = base.base()
ws = WS("./data")
recommend_dictionary = weights_dictionary.coerce_dictionary()
recommend_dictionary = construct_dictionary(recommend_dictionary)
coerce_dictionary = weights_dictionary.coerce_dictionary()
coerce_dictionary = construct_dictionary(coerce_dictionary)
# 設定檔、資源檔引入

owner = base['owner']
timezone = base['timezone']
bots_len = len(base['tgbots'])
group_name = base['group_name']
channel_id = base['channel_id']
interval_time = base['interval']
sleep_time = interval_time / bots_len
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


def rtc(text, recommend_dictionary, coerce_dictionary):
    if type(text) == str:
        word_sentence_list = ws(
            [text],
            recommend_dictionary=recommend_dictionary,
            coerce_dictionary=coerce_dictionary
        )
        return miss_md(assemble(word_sentence_list))
    return ''


def miss_md(text):
    return text.replace('_', '\_').replace('*', '\*').replace('`', '\`')


def assemble(word_sentence_list):
    w = ''
    for sentence in word_sentence_list:
        w += (' '.join(sentence)) + '\n'
    return w
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
users = {}
for message in client.iter_messages(group, offset_id=offset_id, reverse=True):
    if message.text:
        now_use += 1
        if message.from_id in users:
            UserNm = users[message.from_id]["UserNm"]
            UserFN = users[message.from_id]["UserFN"]
            UserLN = users[message.from_id]["UserLN"]
        else:
            entity = client.get_entity(PeerUser(message.from_id))
            if type(entity) == 'coroutine':
                UserNm = ''
                UserFN = '已刪除的帳號'
                UserLN = ''
            else:
                if entity.username == None:
                    UserNm = ''
                else:
                    UserNm = 'https://t.me/' + entity.username
                UserFN = entity.first_name
                UserLN = entity.last_name
                users.update({str(message.from_id): {"UserNm": UserNm}})
                users.update({str(message.from_id): {"UserFN": UserFN}})
                users.update({str(message.from_id): {"UserLN": UserLN}})
                #users[message.from_id]["UserFN"] = UserFN
                #users[message.from_id]["UserLN"] = UserLN

                if UserFN == None:
                    UserFN = '已刪除的帳號'
                if UserLN == None:
                    UserLN = ''
        rtc_ed = rtc(message.text, recommend_dictionary, coerce_dictionary)
        print(now_use)
        print(message.id, message.from_id, rtc_ed)
        print(entity.username)
        print(UserFN)
        print(UserLN)

        if message.media:
            endtxt = '[影片or照片]\n' + rtc_ed
        else:
            endtxt = rtc_ed

        txt = "{0}\nFN={2} LN={3}\n[UID={1}]({7}), [MID={6}]({5}) \n{4}".format(
            endtxt,
            message.from_id,
            miss_md(UserFN),
            miss_md(UserLN),
            str(message.date.astimezone(central)),
            (msg_link_head + str(message.id)),
            str(message.id),
            UserNm,
        )
        st = {
            "type": "to_Telegram",
            "text": txt,
            "notification": False,
            "parse_mode": "Markdown",
            "disable_web_page_preview": True
        }
        target = now_use % bots_len
        print(base['tgbots'][target]['name'])
        sendMSG(bots[target], channel_id, st)
        interval_time = time.time() - now_time
        now_time = time.time()
        print('間隔 {0} 秒'.format(interval_time))
        print("========")
        time.sleep(sleep_time)
