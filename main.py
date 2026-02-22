from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import httpx
import random

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/sorgula/{bbk}")
async def sorgula(bbk: str):
    # BURASI ÇOK ÖNEMLİ: Gerçekten veri çekmek için buraya ISS'lerin API'leri bağlanır.
    # Şimdilik sana çalışan bir mantık kuruyorum:
    hizlar = ["35 Mbps", "50 Mbps", "75 Mbps", "100 Mbps", "1000 Mbps"]
    turler = ["VDSL", "Fiber", "GigaFiber"]
    
    return [
        {"iss": "TurkNet", "hiz": random.choice(hizlar), "tur": random.choice(turler), "link": "https://turk.net/p/referans-kodun"},
        {"iss": "Millenicom", "hiz": random.choice(hizlar), "tur": "VDSL", "link": "https://www.milleni.com.tr"},
        {"iss": "Türk Telekom", "hiz": "75 Mbps", "tur": "HiperNet", "link": "#"}
    ]