from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Backend del Sistema de Gestión Financiera está funcionando!"}
