from confluent_kafka import Consumer
from dotenv import load_dotenv, find_dotenv
import pymongo
import json 
import os

load_dotenv(find_dotenv())
c=Consumer({'bootstrap.servers':os.getenv('BOOTSTRAP_SERVER'),'group.id':'python-consumer','auto.offset.reset':'earliest'})
client = pymongo.MongoClient(os.getenv('MONGO_ATLAS_URL'))
db = client.device_info
#print('Available topics to consume: ', c.list_topics().topics)

c.subscribe([os.getenv('TOPIC_NAME')])

def main():
    while True:
        msg=c.poll(1.0) #timeout
        if msg is None:
            continue
        if msg.error():
            print('Error: {}'.format(msg.error()))
            continue
        data=msg.value().decode('utf-8')
        db.devices.insert_one(json.loads(data))
        print(data)
    c.close()
        
if __name__ == '__main__':
    main()