from fastapi import APIRouter


router = APIRouter(
    prefix="/notes",
    tags=["notes"],
    responses={404: {"description": "Not found"}},
)



@router.get("/")
async def read_records():
    pass

@router.post("/")
async def create_record():
    pass