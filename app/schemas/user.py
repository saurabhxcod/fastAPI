from pydantic import BaseModel,Field
class UserDTO(BaseModel):
    firstName:str=Field(...,example="Saurabh",min_length=2,max_length=10)
    lastName:str=Field(...,example="Singh")
    city:str=Field(...,example="Patna")
    age:int=Field(...,example=25)
    active:bool=Field(...,example=True)