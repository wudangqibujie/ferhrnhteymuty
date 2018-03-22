import requests
from lxml import etree
url = "https://www.xin.com/beijing/biaozhi/"
r = requests.get(url)
with open("test.html","w",encoding="utf-8") as f:
    f.write(r.text)
