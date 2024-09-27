from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    if item_id < 1:
        raise HTTPException(status_code=400, detail="Invalid item ID")
    return {"item_id": item_id, "q": q}

@app.post("/items/")
async def create_item(item: dict):
    if "name" not in item:
        raise HTTPException(status_code=400, detail="Missing 'name' in item")
    return {"item": item, "message": "Item created successfully"}
