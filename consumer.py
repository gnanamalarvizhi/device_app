from confluent_kafka import Consumer
import pymongo
import json 

################

c=Consumer({'bootstrap.servers':'localhost:9092','group.id':'python-consumer','auto.offset.reset':'earliest'})
client = pymongo.MongoClient("mongodb+srv://device_user:device_password@cluster0.zjihjqh.mongodb.net/?retryWrites=true&w=majority")
db = client.device_info
print('Available topics to consume: ', c.list_topics().topics)

c.subscribe(['test_event'])

################

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