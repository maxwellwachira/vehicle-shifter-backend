# Normal way
def userEntity(item) -> dict:
    return {
        
        "name":item["name"],
        "email":item["email"],
        "password":item["password"],
        "mobile":item["mobile"]
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]
