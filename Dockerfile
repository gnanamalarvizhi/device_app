FROM python:3.10
WORKDIR /projects
COPY ./requirements.txt /projects/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /projects/requirements.txt
COPY ./.env /projects/
copy ./app /projects/app
CMD ["uvicorn", "app.main:device_app", "--host", "0.0.0.0", "--port", "5000"]
