from config.database import conn 
from models.user import User
from schemas.user import usersEntity

from passlib.context import CryptContext


def find_all_users():
    return usersEntity(conn.vehicle_shifter.user.find())

def user_exists(email):
    result = conn.vehicle_shifter.user.find_one({"email": email})
    if result is None:
        return False
    else:
        return True

def find_one_user(email):
    if (user_exists(email)):
        return usersEntity(conn.vehicle_shifter.user.find({"email": email}))
    return {"message": "user not found"}


def create_user(user: User):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    dict_user = dict(user)
    dict_user["password"] =  pwd_context.hash(user.password)
    dict_user["account_type"] = "user"
    dict_user["verified_account"] = False
    dict_user["disabled"] = False

    try:
        conn.vehicle_shifter.user.insert_one(dict_user)
        return {"message": "success"}
    except Exception as error:
        return {"message": error}


def update_user(email, user: User):
    if(user_exists(email)):       
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        dict_user = dict(user)
        dict_user["password"] =  pwd_context.hash(user.password)
 
        try:
            conn.vehicle_shifter.user.find_one_and_update({"email": email},{
                "$set":dict_user
            })
            return {"message": "success"}
        except Exception as error:
            return {"message": error}

    return {"message": "user not found"}


def delete_user(email):
    if(user_exists(email)):
        try:
            conn.vehicle_shifter.user.find_one_and_delete({"email": email})
            return {"message": "success"}
        except Exception as error:
            return {"message": error}

    return {"message": "user not found"}
    