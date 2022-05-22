import requests as req
import json

url='https://mis.taifex.com.tw/futures/api/getQuoteList'

payload={"MarketType":"0",
         "SymbolType":"F",
         "KindID":"1",
         "CID":"",
         "ExpireMonth":"",
         "RowSize":"全部",
         "PageNo":"",
         "SortColumn":"",
         "AscDesc":"A"}
headers={
    'Content-Type':'application/json;charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}

resp=req.post(url,data=json.dumps(payload),headers=headers)
print(resp.json()['RtData']['QuoteList'])