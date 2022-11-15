Installation
1. pymongo
pip install fastapi
pip install "uvicorn[standard]"
pip install jinja2
pip install python-multipart
pip3 install pymongo[srv]
pip3 install confluent-kafka
pip install python-dotenv
Database 
This application use mongodb
connect mongodb using compass

mongodb+srv://device_user:device_password@cluster0.zjihjqh.mongodb.net/?retryWrites=true&w=majority

To start zookeeper server
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
To start kafka server
.\bin\windows\kafka-server-start.bat .\config\server.properties

localhost port 2181, while Kafka Server runs on the localhost 9092 port.
To create topics using CLI
kafka-topics.bat --create --topic test-events --bootstrap-server localhost:9092
To list topics using CLI
kafka-topics.bat --describe --topic test-events --bootstrap-server localhost:9092
Send to producer
kafka-console-producer.bat --topic test-events --bootstrap-server localhost:9092
This is my first event
To receive at the consumer part
kafka-console-consumer.bat  --topic test-events --from-beginning --bootstrap-server localhost:9092
This is my second event

To start docker using cli
docker-compose up -d
To run docker container
docker run -d --name device_app -p 80:80 scm