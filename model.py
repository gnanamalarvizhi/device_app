from pydantic import BaseModel

class user(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    confirm_password: str

class shipment(BaseModel):
    shipment_name: str
    shipment_status: str| None = None
    container_no: int | None = None
    route_type: str| None = None
    delivery_type: str| None = None
