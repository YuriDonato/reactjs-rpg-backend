from fastapi import APIRouter, HTTPException
from infra.item import Item, ItemFirebase

router = APIRouter()
item_service = ItemFirebase()

@router.post("/", response_model=Item, summary='Cria um item', description='Cria um item')
async def create_item(item: Item):
    try:
        result = item_service.criar_item(item)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{item_id}", response_model=Item, summary='Obtem um item', description='Obtem um item')
async def read_item(item_id: str):
    if not item_id:
        raise HTTPException(status_code=400, detail="Requer ID para leitura")
    try:
        result = item_service.obter_item(item_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.put("/{item_id}",response_model=Item , summary='Atualiza um item', description='Atualiza um item')
async def update_item(item_id: str, item: Item):
    if not item_id:
        raise HTTPException(status_code=400, detail="Requer ID para atualização")
    try:
        result = item_service.atualizar_item(item_id, item)
        return result
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{item_id}", response_model=Item, summary='Deleta um item', description='Deleta um item')
async def delete_item(item_id: str):
    if not item_id:
        raise HTTPException(status_code=400, detail="Requer ID para exclusão")
    try:
        item_service.deletar_item(item_id)
        return {"message": "Item deletado com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
