from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google.cloud import firestore
from google.oauth2 import service_account

# Cria as credenciais a partir do arquivo serviceAccountKey.json
credentials = service_account.Credentials.from_service_account_file("serviceAccountKey.json")

# Inicializa o cliente do Firestore utilizando as credenciais
db = firestore.Client(credentials=credentials)

app = FastAPI()


# Modelo de dados utilizando Pydantic
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    in_stock: bool = False


# CREATE: cria um novo documento na coleção "items"
@app.post("/items/")
async def create_item(item: Item):
    if not item:
        raise HTTPException(status_code=400, detail="Requer Item")
    if not item.name:
        raise HTTPException(status_code=400, detail="Requer nome")
    if not item.price:
        raise HTTPException(status_code=400, detail="Requer preco")
    doc_ref = db.collection("items").document()
    doc_ref.set(item.dict())
    return {"id": doc_ref.id, **item.dict()}


# READ: recupera um item pelo ID
@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if not item_id:
        raise HTTPException(status_code=400, detail="Requer ID para leitura")
    doc_ref = db.collection("items").document(item_id)
    doc = doc_ref.get()
    if not doc.exists:
        raise HTTPException(status_code=404, detail="Item nao encontrado")
    return doc.to_dict()


# UPDATE: atualiza um item existente
@app.put("/items/{item_id}")
async def update_item(item_id: str, item: Item):
    if not item_id:
        raise HTTPException(status_code=400, detail="Requer ID para atualizacao")
    doc_ref = db.collection("items").document(item_id)
    if not doc_ref.get().exists:
        raise HTTPException(status_code=404, detail="Item nao encontrado")
    doc_ref.update(item.dict())
    return {"id": item_id, **item.dict()}


# DELETE: remove um item pelo ID
@app.delete("/items/{item_id}")
async def delete_item(item_id: str):
    if not item_id:
        raise HTTPException(status_code=400, detail="Requer ID para exclusao")
    doc_ref = db.collection("items").document(item_id)
    if not doc_ref.get().exists:
        raise HTTPException(status_code=404, detail="Item nao encontrado")
    doc_ref.delete()
    return {"message": "Item deletado com sucesso"}
