from fastapi import FastAPI, Request, Form
from typing import Union
from model import user, shipment
import pymongo
from fastapi.encoders import jsonable_encoder 
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

device_app= FastAPI()
device_app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

client = pymongo.MongoClient("mongodb+srv://device_user:device_password@cluster0.zjihjqh.mongodb.net/?retryWrites=true&w=majority")
db = client.device_info

@device_app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@device_app.get('/user/signin')
def signin_users(request: Request):
    return templates.TemplateResponse("signin.html", {"request": request})

@device_app.get('/dashboard')
def dashboard(request: Request):
        return templates.TemplateResponse("dashboard.html", {"request": request, 'shipments': get_all_shipments()})

@device_app.get('/shipment/create')
def shipment_create(request: Request):
    return templates.TemplateResponse("shipment_create.html", {"request": request})

@device_app.post('/users')
def create_users(first_name: str = Form(), last_name: str = Form(), email: str = Form(), password: str = Form(), confirm_password: str = Form()):
    User = user(first_name=first_name,last_name=last_name, email=email, password=password, confirm_password=confirm_password )
    user_data = jsonable_encoder(User)
    if password != confirm_password:
        return {'message':'password and confirm_password shouldnot  match.'}
    elif(db.users.count_documents({ 'email': email}, limit = 1) != 0):
            return {'message':'User already exists in this email'}
    db.users.insert_one(user_data)
    return {'message': 'User created successfully.'}

@device_app.post('/shipments')
def create_shipments(shipment_name: str = Form(),container_no: str = Form(),route_type: str = Form(), delivery_type: str = Form()):
    Shipment = shipment(shipment_name=shipment_name, shipment_status='created', container_no=container_no, route_type=route_type, delivery_type=delivery_type)
    shipment_data = jsonable_encoder(Shipment)
    db.shipments.insert_one(shipment_data)
    return dashboard(shipment_data )

def get_all_shipments():
    shiptments = db.shipments.find()
    return shiptments

@device_app.post("/signin")
def check_user_exists(request: Request, email: str = Form(), password: str = Form(),):
    print(email)
    if(db.users.count_documents({ 'email': email, 'password':password}, limit = 1) != 0):
        return templates.TemplateResponse("dashboard.html", {"request": request, 'shipments': get_all_shipments()})
    return {'message' : 'Incorrect email and password.'}