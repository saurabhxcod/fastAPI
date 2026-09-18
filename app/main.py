from fastapi import FastAPI
from .schemas.api import ApiResponse

app = FastAPI()

@app.get("/",response_model=ApiResponse)
def home():
    response=ApiResponse(message="Welcome to API ",success=True,status="OK")
    return response
@app.get("/about")
def about():
    return {"This is a about page"}   

@app.get("/contact")
def contact():
    return {"This is a contact page"}

@app.get("/get-users")
def get_users():
    return [
        "Saurabh",'Amit','Abhishek','Abhi   '
    ]



