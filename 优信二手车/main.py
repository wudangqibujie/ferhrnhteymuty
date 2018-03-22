import master
import redis_or
import slave
from lxml import etree

# a=master.Master_Spider("shenzhen")
# html = a.get_html("https://www.xin.com/beijing/benchi/i3/")
# urls=a.get_detail_url(html)
q = redis_or.Redis_Data()
# for url in urls:
#     q.set_into_data("test_car_urls",url)
for i in range(1,11):
    url = q.pop_data("test_car_urls")
    # print(url)
    html = master.Master_Spider("shenzhen").get_html("https://"+url)
    print(type(html))
    a = slave.Slave_Spisder()
    data = a.parse_detail_data(html)
    print(data)
