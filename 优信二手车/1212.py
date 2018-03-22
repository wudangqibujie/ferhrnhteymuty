import requests
from lxml import etree
HEADERS = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36","Accept":"*/*","Accept-Encoding": "gzip, deflate, br","X-Requested-With": "XMLHttpRequest","Referer": "https://www.xin.com/40d0nv9ky9/che68276154.html?channel=a49b117c44837d110753e751863f53","Connection": "keep-alive","Host": "www.xin.com"}

r = requests.get("https://www.xin.com/ajax/home_recommend/?uid=fda5d682-d15c-d438-7021-bb8db7537ab3&cityid=3101",headers = HEADERS)
# r.encoding = "ASCII"
print(r.text)
# print(hex(ord("车")))
# print([hex(ord(i)) for i in list("车况检测员")])
# print([chr(i) for i in [0x8f66,0x51b5,0x68c0]])
aa = r.text
bb = aa.encode("utf-8").decode("unicode_escape")
cc = eval(bb)
print(type(cc))
print(cc)
