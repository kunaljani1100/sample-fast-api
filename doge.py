from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/doge/savings")
async def get_savings():
    json = requests.get("https://api.doge.gov/savings/grants")
    return len(json.json()["result"]["grants"])
