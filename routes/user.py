from fastapi import APIRouter, Depends
from models.user import User
from crud import user
from auth import auth


router = APIRouter(
    prefix="/users",
    tags=["users"],
)

#Read All users
@router.get("/")
async def read_all_users(current_user : User = Depends(auth.get_current_user)):
    print(current_user)
    return user.find_all_users()

#Read me
@router.get("/me")
async def read_user_me(current_user : User = Depends(auth.get_current_user)):
    return  current_user
   

#Read one user
@router.get("/{email}")
async def read_one_user(email: str, current_user : User = Depends(auth.get_current_user)):
    return user.find_one_user(email)


#Create user
@router.post("/")
async def add_user(data: User, current_user : User = Depends(auth.get_current_user)):
    if (user.user_exists(data.email)):
        return {"message": "Email Exists"}
    return user.create_user(data)

#Edit user details
@router.put("/{email}")
async def edit_user_details(email, data: User, current_user : User = Depends(auth.get_current_user)):
    return user.update_user(email, data)

#Delete user 
@router.delete("/{email}")
async def delete_user(email: str, current_user : User = Depends(auth.get_current_user)):
    return user.delete_user(email)

