from typing import Optional
from fastapi import FastAPI

app = FastAPI()

# ルート
@app.get("/")
async def index():
    return {"message": "Hello World"}

#パスパラメータ
@app.get("/countries/{country_name}")
async def country(country_name:str):
    return {"country_name": country_name}

#クエリパラメータ
@app.get("/country/")
async def country(country_name:str = "america", country_no:int="new_york"):
    return {
        "country_name": country_name,
        "country_no": country_no
        }

#パスパラメータとクエリパラメータ
@app.get("/countries/{country_name}")
async def country(country_name:str = "", city_name:str=""):
    return {
        "country_name": country_name,
        "city_name": city_name
        }

#オプショナルの場合
@app.get("/countries/")
async def country(country_name:Optional[str] = None, country_no:Optional[int]=None):
    return {
        "country_name": country_name,
        "country_no": country_no
        }
