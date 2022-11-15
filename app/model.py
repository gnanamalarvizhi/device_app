from pydantic import BaseModel

class user(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    confirm_password: str

class shipment(BaseModel):
    shipment_no: int
    container_no: int | None = None
    shipment_description: str| None = None
    phone_no: str| None = None
    delivery_no: int | None = None
    ndc_no: int | None = None
    batch_id: int | None = None
    goods_no: int | None = None
    route_details: str| None = None
    goods_type: str| None = None
    device: str| None = None
    date: str| None = None
