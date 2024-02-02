# coding: UTF-8
import requests
import urllib.request, urllib.error
from bs4 import BeautifulSoup

# アクセスするURL
url = "https://lines-spi.education.ne.jp/compecc/web-cab/description/class/3/id/3/step/1"

# URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
html = requests.get(url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html.text, "html.parser")

session = requests.Session()

payload = {
    "user_id": "2210040",
    "password": "1444"
}

r = session.post("https://lines-spi.education.ne.jp/compecc/user/login", data=payload)
soup = BeautifulSoup(r.content, "html.parser")

correctList = []

for i in range(31):
    t = session.get("https://lines-spi.education.ne.jp/compecc/web-cab/description/class/3/id/3/step/" + str(i))
    soup = BeautifulSoup(t.content, "html.parser")

    soup = soup.find_all("label", class_="radio-label")
    for i in soup:
        # print("text", i)
        correct = i.find("span", class_="p-option correct")
        if(correct != None):
            correct = i.find("span", class_="radio-text")
            correctList.append(correct.decode_contents(formatter="html"))

for i in range(len(correctList)):
    list_item = correctList[i]
    print(f"{i+1}問: {list_item}")


