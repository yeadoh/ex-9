from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import HTMLResponse

app = FastAPI()
@app.get("/")
async def debug_path(request: Request):
    return {"msg": "OK"}
