from confluent_kafka import Producer
from dotenv import load_dotenv, find_dotenv
import socket    
import time    
import os
import json 

load_dotenv(find_dotenv())
s = socket.socket() 
s.connect((os.getenv('SOCKET_SERVER_HOST'), int(os.getenv('SOCKET_SERVER_PORT'))))
p=Producer({'bootstrap.servers':os.getenv('BOOTSTRAP_SERVER')})

while True:
	try:
		data=s.recv(70240).decode()
		json_acceptable_string = data.replace("'", "\"")
		d = json.loads(json_acceptable_string)
		
		for i in d:
			result=json.dumps(i)
			p.produce(os.getenv('TOPIC_NAME'),result.encode('utf-8'))
#			#print(result)
	except Exception as e:
		print(e)
s.close() 