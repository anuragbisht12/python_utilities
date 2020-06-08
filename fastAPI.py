from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import joblib,os

yourmodel=open('LOCATION','rb')
model=joblib.load(yourmodel)

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None
    
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def create_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

# ML function, you can customize as per your needs
@app.get("/predict/{item_id}")
def predict(item_id):
    prediction=model.predict([item_id])
    return {"item_id":item_id, "prediction":prediction}

if __name__=='__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)

#run server either calling the python file or using below command  
# uvicorn fastapi_main:app --reload
