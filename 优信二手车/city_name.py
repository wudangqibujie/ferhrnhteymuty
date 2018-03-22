import requests
from lxml import etree
import json

HEADERS = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36","Accept":"*/*","Accept-Encoding": "gzip, deflate, br","X-Requested-With": "XMLHttpRequest","Referer": "https://www.xin.com/40d0nv9ky9/che68276154.html?channel=a49b117c44837d110753e751863f53","Connection": "keep-alive","Host": "www.xin.com"}
def get_city_id():
    url = "https://www.xin.com/ajax/top_load?ename=2401"
    r = requests.get(url,headers = HEADERS)
    data = r.text
    city_id1 = data.encode("utf-8").decode("unicode_escape")
    city_id2 = eval(city_id1)
    city_id = city_id2["half_city"]
    city_id = [str(i)+'\n' for i in city_id]
    return city_id
def save_city_id(id_list):
    f = open("city_id.txt","w")
    f.writelines(id_list)
    f.close()

def get_citr_name(ID):
    url = "https://www.xin.com/ajax/home_recommend/?uid=fda5d682-d15c-d438-7021-bb8db7537ab3&cityid="+ID
    r = requests.get(url,headers = HEADERS)
    data = r.text
    city_id1 = data.encode("utf-8").decode("unicode_escape")
    city_id2 = eval(city_id1)
    city_ename = city_id2["city"]["ename"]
    return  city_ename
def city_dict():
    id_ename = dict()
    ids = get_city_id()
    for i in ids:
        try:
            ename = get_citr_name(str(i))
            id_ename[i.strip()] = ename
        except KeyError:
            print("无效ID",i)
            continue
        except:
            print("其他异常",i)
            continue
    return  id_ename
def citydict2json(dic):
    # json_ename = json.dumps(dic)
    f = open("ename_jso.json","w")
    json.dump(dic,f)
    f.close()

def json2citydict():
    # ename_dic = json.loads(jso)
    f = open("ename_jso.json","r")
    dic = json.load(f)
    f.close()
    return dic
if __name__ == '__main__':
    a=json2citydict()
    print(a)
    j=0
    for i in a:
        j += 1
    print(j)




