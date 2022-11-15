FROM python:3.10
WORKDIR /projects
RUN pip install --no-cache-dir --upgrade pip &&pip install --no-cache-dir python-dotenv
COPY ./.env .
COPY ./server.py .
CMD [ "python", "./server.py"]