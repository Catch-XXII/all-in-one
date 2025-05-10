from fastapi import APIRouter

router = APIRouter()


@router.get("/hello")
async def hello(name: str = "world"):
    return {"message": f"Hello, {name}!"}
