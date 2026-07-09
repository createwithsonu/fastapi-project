from fastapi import FastAPI
#Using Pydantic
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: str
@app.post("/users")
def create_user(user:User):
    return{
        "message": "User created successfully !",
        "user": user
    }