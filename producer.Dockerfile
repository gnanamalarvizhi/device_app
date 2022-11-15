FROM python:3.10
WORKDIR /projects/app
RUN pip install --no-cache-dir --upgrade pip &&pip install --no-cache-dir confluent-kafka python-dotenv
COPY ./.env .
COPY ./client.py ./
CMD [ "python", "./client.py"]