import requests

def newip():
    print("正在获取新的代理IP")
    url = ""
    response = requests.get(url)
    response.raise_for_status()
    newip = "http://"+response.text.split("\n")[0]
    print("新的代理IP为:"+newip)
    return newip

