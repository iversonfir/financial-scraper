from requests import get
import json

resp=get('https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=json&date=20220520&selectType=30&_=1653231786746')
dataJson=resp.json()
print(dataJson['data'])