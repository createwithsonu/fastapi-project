from fastapi import FastAPI, status, HTTPException

app = FastAPI()

@app.post("/create-user", status_code=status.HTTP_201_CREATED)
def create_user():
    return {"message": "User created successfully."}

@app.get("/users")
def get_users():
    return {
        "Status": "Success",
        "Message": "Users retrieved successfully.",
        "Data":{
            "Name":"Sonu Patel",
            "Age":25
        }
    }

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id != 1:
        raise HTTPException(
            status_code=404, 
            detail="User not found."
            )
    return {
        "id":1,
        "name":"Sonu Patel"
    }
