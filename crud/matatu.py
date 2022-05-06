from config.database import conn 
from schemas.matatu import serializeList, serializeDoneList

def find_all_matatus():
    return serializeList(conn.local.matatu.find())

def find_one_matatu(reg):
    if (matatu_exists(reg)):
        return serializeList(conn.local.matatu.find({"reg": reg}))
    return {"message": "matatu not found"}


def matatu_exists(reg):
    result = conn.local.matatu.find_one({"reg": reg})
    if result is None:
        return False
    else:
        return True

def create_matatu(matatu):
    if(matatu_exists(matatu.reg)):
       return {"message": "matatu exists"}
    try:
        conn.local.matatu.insert_one(dict(matatu))
        return {"message": "success"}
    except Exception as error:
        return {"message": error}


def update_matatu(reg, matatu):
    if(matatu_exists(reg)):       
        try:
            conn.local.matatu.find_one_and_update({"reg": reg},{
                "$set":dict(matatu)
            })
            return {"message": "success"}
        except Exception as error:
            return {"message": error}

    return {"message": "matatu not found"}


def delete_matatu(reg):
    if(matatu_exists(reg)):
        try:
            conn.local.matatu.find_one_and_delete({"reg": reg})
            return {"message": "success"}
        except Exception as error:
            return {"message": error}

    return {"message": "matatu not found"}

def find_waiting_matatus():
    return serializeList(conn.local.waiting.find({"status": "waiting"}))


def add_matatu_waiting(matatu_list):
    repeated_values = []
    index = 0
    for matatu in matatu_list:
        result = conn.local.waiting.find_one({"reg": matatu.reg, "date": matatu.date})
        if result is not None:
            repeated_values.append(index)
        index = index + 1

    if len(repeated_values) > 0:
        for i in repeated_values:
            matatu_list.pop(i)

    if len(matatu_list) == 0:
        return {"message": "Duplicate Items"}

    try:
       for matatu in matatu_list:
           conn.local.waiting.insert_one(dict(matatu))

       return {"message": "success"}

    except Exception as error:
        return {"message": error}

def delete_matatu_waiting(reg):
    try:
        conn.local.waiting.find_one_and_delete({"reg": reg})
        return {"message": "success"}
    except Exception as error:
        return {"message": error}

def update_waiting_status(reg, data):
    try:
        conn.local.waiting.find_one_and_update({"reg": reg},{
            "$set": {"status": "done", "done_date": data.date, "done_time": data.time}
        })
        return {"message": "success"}
    except Exception as error:
        return {"message": error}

def find_done_matatus():
    return serializeDoneList(conn.local.waiting.find({"status": "done"}))


def search_matatu(search_term):
    if search_term is None:
        find_all_matatus()
    else:
        try:
            result = conn.local.matatu.find({"$or": [{"reg": search_term}, {"driver": search_term.capitalize()}, {"stage": search_term.capitalize()}, {"to": search_term.capitalize()}]})
            if result is None:
                return {"message": "Not Found"}
            return serializeList(result)
        except Exception as error:
            return {"message": error}

    