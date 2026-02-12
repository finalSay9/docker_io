from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Bank(BaseModel):
    bank_name: str
    account_type: str
    accountNo: int
    isOwner: bool = None

@app.get("/")
def home():
    return {"message": "Hello Docker"}


@app.post('/bank', response_model=Bank)
def createAcc(account: Bank) -> Bank:
    return account

@app.post('use_bank', response_model=Bank)
def useBank():
    return {
        "bank name": "fdh",
        "account type": "current",
        "account": 123487,
        "is owner": True
    }
