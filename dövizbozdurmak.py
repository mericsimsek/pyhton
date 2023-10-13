import requests
import json

web="https://api.exchangeratesapi.io/v1/latest?base="

istenendöv=input("İstenen döviz türü gir:")
alınandöv=input("Almak istediğin döviz türü gir:")
miktardöv=int(input(f"Kaç lot {istenendöv} almak istediğini gir:"))

want=requests.get(web+istenendöv)
want=json.loads(want.text)

print("1 {0}={1}{2}".format(istenendöv,want["rates"][alınandöv],alınandöv))
print("{0} {1}={2}{3}".format(miktardöv,istenendöv,miktardöv*want["rates"][alınandöv]))