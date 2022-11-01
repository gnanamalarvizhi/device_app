from confluent_kafka import Producer
import socket    
import time    
import json 
s = socket.socket() 
HOST = "127.0.0.1"
PORT = 12345               
s.connect((HOST, PORT))
p=Producer({'bootstrap.servers':'localhost:9092'})

while True:
	try:
		data=s.recv(70240).decode()
		json_acceptable_string = data.replace("'", "\"")
		d = json.loads(json_acceptable_string)
		
		for i in d:
			result=json.dumps(i)
			p.produce('test_event',result.encode('utf-8'))
			#print(result)
	except Exception as e:
		print(e)
s.close() 