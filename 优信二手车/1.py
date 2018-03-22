

#以下用于断点爬虫的应用
import redis
import time
r = redis.Redis(host="localhost",port = "6379")
def A():
    r.lpush("FT","bmw")
    for i in range(100):
        r.lpush("FT",str(i))

def B():
    a=r.brpop("FT",1)
    print(a)

def C():
    r.lpush("ABT","bmw")
def D():
    a=r.brpop("ABT",10)
    print(a)

if __name__ == '__main__':
    C()




