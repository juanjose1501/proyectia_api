from typing import Dict
from pydantic import BaseModel

class ProyectoInDB(BaseModel):
    nombre: str
    empresa: str
    descripcion: str
    fases: str
    fecha_inicio: str
    fecha_fin: str
    presupuesto: int
    encargado: str
    num_personas: int
    horas_estimados: int
    

database_proyecto = Dict[str, ProyectoInDB]
database_proyecto = {
    "estructuras1": ProyectoInDB(**{"nombre":"estructuras1",
                                "empresa":"Cartones Lopez",
                                "descripcion":"Remodelacion de la estructura física de la empresa",
                                "fases":"2",
                                "fecha_inicio":"15/11/2020",
                                "fecha_fin": "15/12/2020",
                                "presupuesto":2000000,
                                "encargado":"Juan Peña",
                                "num_personas":4,
                                "horas_estimados":192}),
    "campaniasalento": ProyectoInDB(**{"nombre":"campaniasalento",
                                "empresa":"Artesanos Cafeteros",
                                "descripcion":"Lanzamiento campaña basada en el municipio de Salento",
                                "fases":"1",
                                "fecha_inicio":"24/04/2020",
                                "fecha_fin":"24/08/2020",
                                "presupuesto":5300000,
                                "encargado":"Maria Rodriguez",
                                "num_personas":2,
                                "horas_estimados":768}),
    "proyectocarros": ProyectoInDB(**{"nombre":"proyectocarros",
                                "empresa":"Metric Software",
                                "descripcion":"Creación página web para la compraventa de carros",
                                "fases":"3",
                                "fecha_inicio":"12/06/2020",
                                "fecha_fin":"12/12/2020",
                                "presupuesto":10000000,
                                "encargado":"Juan José Montoya",
                                "num_personas":3,
                                "horas_estimados":1152})

}

def get_proyecto(nombre: str):
    if nombre in database_proyecto.keys():
        return database_proyecto[nombre]
    else:
        return None

def update_proyecto(proyecto_in_db: ProyectoInDB):
    database_proyecto[proyecto_in_db.nombre] = proyecto_in_db
    return proyecto_in_db

def get_all():
    lista_proyectos = []
    for ProyectoInDB in database_proyecto:
        lista_proyectos.append(database_proyecto[ProyectoInDB])
    return lista_proyectos

def create_proyecto(proyecto:ProyectoInDB):
    if proyecto.nombre in database_proyecto:
        return False
    else:
        database_proyecto[proyecto.nombre] = proyecto

def delete_proyecto(proyecto: str):
    if proyecto in database_proyecto:
        del database_proyecto[proyecto]
        return True 
    else:
        return False         



