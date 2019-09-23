def base():
    return {
        "owner": 123456789, # 你的UID
        "group_name": 'LINE', # 如名，但其實能讓telethon獲得實體的東西都可以
        "channel_id": int(-100123456789), #你新創要丟紀錄的頻道
        "userbot": {
            # 請自己去 https://my.telegram.org/auth
            # 登入後在API development tools 申請
            "api_id": 1234567,
            "api_hash": 'XXX'
        },
        "tgbots": [
            # 乾... 枉費我這精美的陣列，結果同群1分鐘所有tgbot僅能發20封
            {
                "name": "@OOO_bot",
                "token": "123123:ABC"
            }, {
                "name": "@XXX_bot",
                "token": "456456:DFG"
            },
        ],
        "timezone": "Asia/Taipei",
        "interval": 4.05, # 決定bots發送頻率的微妙參數。
    }
