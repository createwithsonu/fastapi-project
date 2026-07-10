from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: User):
    users.append(user)
    return{
"message": "User created successfully", "user": user
    }

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User, notify: bool = False):
#indexing starting from 0 for user_id
    if user_id < len(users):
        users[user_id] = user
        return{
            "Message": "User updated successfully", "data": user, "notify": notify
        }
    return{
        "Error": "User not found"
    }
