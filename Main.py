*main.py*

from fastapi import FastAPI

app = FastAPI()

@app.get("/info")
def read_info():
    return {
        "name": "Parcial 1 Electiva",
        "description": "Proyecto parcial",
        "version": "1.0.0",
        "author": "brayan stiven salazar galvis, salazar.brayan.7149@eam.edu.co"
    }


*requirements.txt*
fastapi
uvicorn
