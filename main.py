from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()

from db.proyecto_db import ProyectoInDB
from db.proyecto_db import update_proyecto, get_proyecto , get_all , create_proyecto
import db.proyecto_db
 
from models.proyecto_models import ProyectoIn, ProyectoOut
from db import proyecto_db

from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080","https://proyectia-app.herokuapp.com"
]
api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)


@api.get("/proyecto/consulta/{nombre}")
async def get_nombre(nombre: str):

    proyecto_in_db = get_proyecto(nombre)
    if proyecto_in_db == None:
            raise HTTPException(status_code=404,
                detail="El proyecto no existe")

    proyecto_out = ProyectoOut(**proyecto_in_db.dict())
    return proyecto_out

@api.post("/proyecto/consulta/")
async def get_datos(proyecto_in: ProyectoIn):

    proyecto_in_db = get_proyecto(proyecto_in.nombre)
 
    if proyecto_in_db == None:
        raise HTTPException(status_code=404,
                detail="El proyecto no existe")
    if proyecto_in_db.empresa != proyecto_in.empresa: 
        raise HTTPException(status_code=403, 
                detail="El proyecto no fue encontrado")
    
    proyecto_out = ProyectoOut(**proyecto_in_db.dict())
    return proyecto_out

@api.get("/proyecto/lista")
async def get_lista():
    return proyecto_db.get_all()

@api.post("/proyecto/crear")
async def crear_proyecto(proyecto_in: ProyectoInDB):
    operacion_exitosa=proyecto_db.create_proyecto(proyecto_in)
    if operacion_exitosa != False:
        return {"Se ha creado el proyecto satisfactoriamente"}
    else:
        raise HTTPException(status_code=400,detail="El proyecto ya existe")
