from fastapi import FastAPI

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sigmotoa FC")


@app.get("/")
async def root():
    return {"message": "sigmotoa FC data"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Bienvenido a sigmotoa FC {name}"}

#RE-3-FORMMULARARIO RIVAL
@app.get("/rivales/{equipo_id}")
async def get_rivals(equipo_id: int ):
    rivales = {
        1: ["VISISTANTE"],
        2: ["LOCAL"],
    }
    return {"equipo_id": equipo_id, "rivales": rivales.get(equipo_id, [])}
