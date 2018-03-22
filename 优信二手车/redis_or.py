import redis

class Redis_Data():
    #redis-py使用connection pool来管理对一个redis server的所有连接，避免每次建立、释放连接的开销。默认，每个Redis实例都会维护一个自己的连接池。可以直接建立一个连接池，然后作为参数Redis，这样就可以实现多个Redis实例共享一个连接池
    # def __init__(self,IP="localhost"):
    #     self.pool = redis.Redis(host=IP,port=6379)
    #     self.r = redis.Redis(connection_pool=self.pool)
    def __init__(self,IP="localhost"):
        self.r = redis.Redis(host=IP,port = 6379,decode_responses=True)
    def set_into_data(self,set_name,data):
        self.r.sadd(set_name,data)
    def pop_data(self,set_name):
        pop_data = self.r.spop(set_name)
        return pop_data

if __name__ == '__main__':
    q = Redis_Data()
    # q.set_into_data("liujie","chenjiajia")
    # q.set_into_data("liujie","chenxiaomi")
    pop = q.pop_data("liujie")
    print(pop)



