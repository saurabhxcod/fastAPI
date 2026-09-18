from fastapi import FastAPI
from .schemas.api import ApiResponse
from .schemas.user import UserDTO
app = FastAPI()

@app.get("/",response_model=ApiResponse)
def home():
    response=ApiResponse(message="Welcome to API ",success=True,status="OK")
    return response
@app.get("/about")
def about():
    return {"This is a about page"}   


@app.post("/users",response_model=ApiResponse)
def create_user(user:UserDTO):
    return ApiResponse(message=f"User {user.firstName} {user.lastName} created successfully",status="OK",success=True)


@app.put("/users/{user_id}/name/{user_name}")
def update_users(user_id:int,user_name:str):
    return ApiResponse(message=f"Updated user {user_name} successfully",status="OK",success=True)

@app.get("/users/search")
def search_users(firstName:str="None",lastName:str="None",age:int=0):
    return ApiResponse(message=f"Users filtered successfully for first name {firstName} and last name {lastName} and age {age}",status="OK",success=True)
    
@app.get("/users/{user_id}")
def get_user(user_id:int):
    return ApiResponse(message=f"User details retrieved successfully for user id {user_id}",status="OK",success=True)


@app.get("/contact")
def contact():
    return {"This is a contact page"}

@app.get("/get-users")
def get_users():
    return [
        "Saurabh",'Amit','Abhishek','Abhi   '
    ]



