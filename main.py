from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class User(BaseModel):
    name: str
    age: int
    password: str

class UserResponse(BaseModel):
    name: str
    age: int
#response_model is used to filter the response data and exclude sensitive information like password.
@app.get("/users/", response_model=UserResponse)
def get_user():
    # Simulate fetching user data from a database
    return {
        "name": "Sonu Patel",
        "age": 30,
        "password": "secret"
    }
