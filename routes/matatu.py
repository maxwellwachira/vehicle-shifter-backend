from typing import List, Optional
from fastapi import APIRouter, Depends
from auth import auth
from models.matatu import Matatu, Date
from models.user import User
from crud import matatu

router = APIRouter(
    prefix="/matatus",
    tags=["matatus"],
)

#Read all matatus 
@router.get("/" )
async def read_matatus (current_user : User = Depends(auth.get_current_user)):
    return matatu.find_all_matatus()

#read matatu waiting List
@router.get("/waiting")
async def read_waiting_matatus():
    return matatu.find_waiting_matatus()

#read matatu done List
@router.get("/done")
async def read_done_matatus():
    return matatu.find_done_matatus()

#read matatu done List
@router.get("/search")
async def search_matatus(query: Optional[str] = None, current_user : User = Depends(auth.get_current_user)):
    return matatu.search_matatu(query)


#read one matatu 
@router.get("/{reg}")
async def read_one_matatu(reg: str, current_user : User = Depends(auth.get_current_user)):
    return matatu.find_one_matatu(reg)
    

#add matatu to waiting List
@router.post("/waiting")
async def add_matatu(data: List[Matatu], current_user : User = Depends(auth.get_current_user)):
    return matatu.add_matatu_waiting(data)

#add one matatu to db
@router.post("/")
async def add_matatu(data: Matatu, current_user : User = Depends(auth.get_current_user)):
    return matatu.create_matatu(data)

#Edit status details
@router.put("/waiting/{reg}")
async def update_status_details(reg: str, date: Date, current_user : User = Depends(auth.get_current_user)):
    return matatu.update_waiting_status(reg, date)

#Edit matatu details
@router.put("/{reg}")
async def edit_matatu_details(reg: str, data: Matatu, current_user : User = Depends(auth.get_current_user)):
    return matatu.update_matatu(reg, data)

#delete matatu 
@router.delete("/waiting/{reg}")
async def delete_matatu_waiting(reg: str, current_user : User = Depends(auth.get_current_user)):
    return matatu.delete_matatu_waiting(reg)

#delete matatu 
@router.delete("/{reg}")
async def delete_matatu(reg: str, current_user : User = Depends(auth.get_current_user)):
    return matatu.delete_matatu(reg)