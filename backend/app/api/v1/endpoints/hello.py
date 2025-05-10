from fastapi import APIRouter

router = APIRouter()


@router.get("/api/v1/hello")
async def hello(name: str = "world"):
    return {"message": f"Hello, {name}!"}
