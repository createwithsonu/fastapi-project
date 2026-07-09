from fastapi import FastAPI
#Using Pydantic
from pydantic import BaseModel
app=FastAPI()
class User(BaseModel):
    name:str
    age:int
@app.post("/create-user")
def create_user(user:User):
    return{
        "Message":"User Created Successfully !",
        "Data":user
    }