from fastapi import APIRouter

router = APIRouter()

# changed @app.get("/") to @router.get("/")
@router.get("/")
async def rootuser():
    return {"message": "Get Userssss!"}

@router.get("/kevin")
async def rootuserkevin():
    return {"message": "Get Kevin User"}