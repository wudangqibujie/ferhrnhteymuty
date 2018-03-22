import pymongo
class Mongo_Data():
    def __init__(self,base_name,ip="localhost"):
        self.client = pymongo.MongoClient(ip,27017)
        self.db = self.client[base_name]
    def get_all_coll_names(self):
        coll_names = self.db.collection_names()
        return coll_names

    def get_collection(self,colle_name,db):
        coll = db[colle_name]
        return coll
    def insert_data2coll(self,data,coll):
        coll.insert(data)
    def remove_coll(self,coll,data,all=False):
        if all:
            coll.remove()
        else:
            coll.remove(data)
    def update_coll(self,coll,old_data,new_data):
        coll.update(old_data,{"$set":new_data})
    def find_one_docum(self,coll):
        one = coll.find_one()
        return one
    def find_multi_docum(self,coll):
        all = coll.find()
        return all
    def get_docum_num(self):
        num = self.find_multi_docum().count()
if __name__ == '__main__':
    fir  = Mongo_Data("BMWAMG")
    coll = fir .get_collection("M5E63",fir.db)
    fir.remove_coll(coll)

    # names = fir.get_all_coll_names()
    # print(names)





