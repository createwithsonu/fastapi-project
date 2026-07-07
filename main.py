from fastapi import FastAPI
app=FastAPI()

#home route
@app.get("/")
def home():
    return {"message": "This is the home page."}

#About route
@app.get("/about")
def about():
    return {"message": "This is the about page."}

#User route
@app.get("/users/{user_id}")
def users(user_id:int):
    return {
        "user_id":user_id
    }
