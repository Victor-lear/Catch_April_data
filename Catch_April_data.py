
import pymongo
from pymongo import MongoClient
import time
from datetime import datetime
import isodate
mongo_url_01="mongodb://admin:bmwee8097218@140.118.122.115:30415/"
def Catchdata(DB, Collection,start_time,end_time):
    global mongo_url_01
    try:
        conn = MongoClient(mongo_url_01) 
       
        db = conn[DB]
        
        collection = db[Collection]
       
        data={"Datetime": {"$gte": start_time,"$lte": end_time}}
        cursor=collection.find(data)
  

        data=[d for d in cursor]
    except:
        data=[]
    if data==[]:
        return False
    else:
        return data
def insertdata(DB,Collection,data):
    global mongo_url_01
    conn = MongoClient(mongo_url_01) 
    db = conn[DB]
    collection = db[Collection]
    cursor = collection.insert_many(data)
timestamp=1680278400
start_time = datetime.fromtimestamp(timestamp)
timestamp=1682870399
end_time= datetime.fromtimestamp(timestamp)
data=Catchdata("AP_test","Collect_Client",start_time,end_time)
print(data[0])
insertdata("AP_test","April_Client",data)
