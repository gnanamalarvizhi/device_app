from fastapi import FastAPI, Request, Form
from .model import user, shipment
import pymongo
from fastapi.encoders import jsonable_encoder 
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv, find_dotenv
import os

device_app= FastAPI()
root_path = os.path.abspath(os.curdir)
device_app.mount("/static", StaticFiles(directory=root_path + "/app/static"), name="static")
templates = Jinja2Templates(directory=root_path + "/app/templates")
load_dotenv(find_dotenv())

client = pymongo.MongoClient(os.getenv('MONGO_ATLAS_URL'))
db = client.device_info

@device_app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@device_app.get('/user/signin')
def signin_users(request: Request):
    return templates.TemplateResponse("signin.html", {"request": request})

@device_app.get('/dashboard')
def dashboard(request: Request):
        return templates.TemplateResponse("dashboard.html", {"request": request})

@device_app.get('/devices')
def devices(request: Request):
        return templates.TemplateResponse("device.html", {"request": request, 'devices': get_all_devices()})

@device_app.get('/shipment/create')
def shipment_create(request: Request):
    return templates.TemplateResponse("shipment_create.html", {"request": request})

@device_app.post('/users')
def create_users(first_name: str = Form(), last_name: str = Form(), email: str = Form(), password: str = Form(), confirm_password: str = Form()):
    User = user(first_name=first_name,last_name=last_name, email=email, password=password, confirm_password=confirm_password )
    user_data = jsonable_encoder(User)
    if(db.users.count_documents({ 'email': email}, limit = 1) != 0):
            return {'message':'User already exists in this email'}
    db.users.insert_one(user_data)
    return {'message': 'User created successfully.'}

@device_app.post('/shipments')
def create_shipments(shipment_no: int= Form(), container_no: int= Form(), shipment_description: str = Form(), phone_no: str = Form(), delivery_no: int= Form(), ndc_no: int= Form(), batch_id: int= Form(), goods_no: int= Form(), route_details: str = Form(), goods_type: str = Form(), device: str = Form(), date: str = Form()):
    Shipment = shipment(shipment_no=shipment_no, container_no=container_no, shipment_description=shipment_description, phone_no=phone_no, delivery_no=delivery_no, ndc_no=ndc_no, batch_id=batch_id, goods_no=goods_no, route_details=route_details, goods_type=goods_type, device=device, date=date)
    shipment_data = jsonable_encoder(Shipment)
    db.shipments.insert_one(shipment_data)
    return dashboard(shipment_data )

def get_all_devices():
    devices= db.devices.find()
    return devices

@device_app.post("/signin")
def check_user_exists(request: Request, email: str = Form(), password: str = Form(),):
    if(db.users.count_documents({ 'email': email, 'password':password}, limit = 1) != 0):
        return templates.TemplateResponse("dashboard.html", {"request": request, 'shipments': get_all_shipments()})
    return {'message' : 'Incorrect email and password.'}