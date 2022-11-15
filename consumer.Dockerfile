FROM python:3.10
WORKDIR /projects/app
RUN pip install --no-cache-dir --upgrade pip &&pip install --no-cache-dir confluent-kafka python-dotenv pymongo[srv]
COPY ./.env .
COPY ./consumer.py ./
CMD [ "python", "./consumer.py"]