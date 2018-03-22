import requests
from lxml import etree

url = "https://www.xin.com/40d0nv9ky9/che68276154.html?channel=a49b117c44837d110753e751863f53"
r = requests.get(url)
html = etree.HTML(r.text)
itm = html.xpath('/html/body/div[2]/div[14]/div/div[4]/div[4]/dl[1]/dd[1]/span[2]/text()')
f = open("bmwwww.html","w",encoding="utf-8")
f.write(r.text)
f.close()
print(itm)
