import urllib.request
import json

#return Bitcoin CAD price change rate over four months
def appr (data):
  ini_date = data[1]
  cur_date = data[0]
  
  value=[]
  url_ini = f'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{ini_date}/v1/currencies/btc.json'

  url_cur = f'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{cur_date}/v1/currencies/btc.json'
  
  ini_req = urllib.request.urlopen(url_ini)
  ini_res = json.loads(ini_req.read())

  # print (ini_res) 

  cur_req = urllib.request.urlopen(url_cur)
  cur_res = json.loads(cur_req.read())
  
  value.append(ini_res["btc"]["cad"])
  value.append(cur_res["btc"]["cad"])
  
  # print(round(value[0],2))

  ch = (value[1] - value[0])/value[0] *100
  return round(ch,2)

#return Bitcoin/CAD excange rate for the current day
def rate (dates) :
  date = dates[0]
  price = []
  url = f'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{date}/v1/currencies/btc.json'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())

  price.append(result["btc"]["cad"])
  rate_res = f'The BTC/CAD exchange rate for {date} is 1BTC : {round(price[0],2)}CAD'
  return rate_res