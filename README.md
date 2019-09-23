# Telegram_search_text_alternative_plan
指望官方改好天知道猴年馬月。透過將訊息轉發至頻道，並傳送"斷詞"後的文字的方式，來讓使用者可以搜尋。

# 截圖(Screenshot)
![Imgur](https://imgur.com/0qkwYAM.png)
![Imgur](https://imgur.com/KgAlftg.png)
![](https://imgur.com/FOiFcaf.png)

# 部屬(Installing)
- 環境:
  python3.6.8 可以，其他未知。

- 函式庫:
  telepot\=\=12.7
  Telethon\=\=1.10.0
-  [ckiptagger](https://github.com/ckiplab/ckiptagger) 所需要的，請自行參考他的文件來選擇適合你電腦的方式。    
(恩對，他的 data 資料請下載後解壓擺跟main.py同目錄)

- config 資料夾內
    * base.py 請填上你的bot...等資料(內有說明便不複述)。
    * weights_dictionary.py是調整字的權重用的，不調也沒差。

- Telegram 端
    * 拉userbot到群組(可能需要將此群組置頂，主要是讓Telethon看見他啦)
    * 把你的bots拉到頻道當管理員(發言權限記得給)


# 執行(start)

```
python main.py
```
執行後 CLI 會要你填 offset_id，剛開始的話0就好，或者看你要從第幾條開始轉發。    
如果是中斷後繼續轉發，則可直接輸入最後的 MID 編號。     


# Q&A

  1. 我要怎麼估算我要多久才能轉傳全部?
    你可以複製你的群組最後一則的"訊息連結"，最後面的數字是你們聊的數量。
    設該數量為X，有效句子參數為Y(假設為0.67)，X/20/60/24*Y 就等於所需的時間。    

      例如公開群組"LINE"他目前有47735則訊息，所以X=477355，然後Y看你的群組訊息文字與非文字比例相除的值(以"LINE"來說，有效文字量為32436，Y=32436/47735=0.679)    
      X(47735)/20/60/24*Y(0.679) = 1.12天 就可以整個轉傳    


# 免責(Disclaimer)
**如用此程式造成TG帳號被刪或其他事故一蓋不負責任。**    

對了，我用獻祭一個帳號換得一個知識，如果想用 userbot 去發，你一但被429一次，沒有第二次...。     


# 感謝(Thank) (\*´∀\`)\~♥
  感謝 唯唯der抱怨，不然還沒想到要做這個東東。    

  感謝 [中研院 Open Source](https://github.com/ckiplab/ckiptagger) 這個斷詞模型，不然我本來是直接 text.replace('', ' ') 解決。     

  感謝 提供測試的2個群組(一隱藏一公開)。     

  感謝 提出格式建議的各位。     

  感謝 [raytracy](https://ithelp.ithome.com.tw/questions/10195361#answer-358640) 大大解惑授權污染的問題。


# 贊助(Donate)
hmmm........     
如果你覺得這對你有幫助的話，........    
聽說這是 "台灣pay" 的 [QRcode](https://i.imgur.com/rVmAnh6.jpg)..............    
但我也沒用過(｡ŏ﹏ŏ) .......................................    

# 作者(Author)
![](https://avatars3.githubusercontent.com/u/22027801?s=460&v=4)    

[永格天](https://we684123.carrd.co/)    
一個~~中二病~~水瓶座男子    
不太擅長塗鴉 (看大頭貼就知道Orz...)    
