from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    roll_no : int
    standard : int 

@app.post("/main")
def postData(item = Item):
    return {"response" : item}

	