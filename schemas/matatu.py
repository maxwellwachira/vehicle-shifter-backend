def serializeDict(item) -> dict:
    return {
        "reg":item["reg"],
        "stage":item["stage"],
        "to":item["to"],
        "fare":item["fare"],
        "driver": item["driver"]
    }

def serializeList(entity) -> list:
    return [serializeDict(item) for item in entity]


def serializeDoneDict(item) -> dict:
    return {
        "reg":item["reg"],
        "stage":item["stage"],
        "to":item["to"],
        "fare":item["fare"],
        "driver": item["driver"],
        "done_time": item["done_time"]
    }

def serializeDoneList(entity) -> list:
    return [serializeDoneDict(item) for item in entity]
