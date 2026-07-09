from fastapi import FastAPI
#Using Pydantic
from pydantic import BaseModel

app = FastAPI()

#Handling Nested JSON data using Pydantic models
class Adress(BaseModel):
    city: str
    state: str
    pincode: int
class User(BaseModel):
    name: str
    age: int
    email: str
    address: Adress
@app.post("/create-User")
def create_user(user:User):
    return{
        "message": "User created successfully !",
        "user": user
    }