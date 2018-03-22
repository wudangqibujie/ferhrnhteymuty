import requests

START_URL = "https://www.xin.com/"
CITY = "shenzhen"
HEADERS = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
def get_html(url):
    try:
        r = requests.get(url,headers = HEADERS)
        if r.status_code == 200:
            return r.text
        else:
            print("相应状态码有异常！")
    except:
        print("请求存在异常!")





if __name__ == '__main__':
    get_html("http://www.baidu.com")
