from fastapi import APIRouter

router = APIRouter()
@router.get("/")
def pagina_inicial():
    return {"message": "Olá"}
