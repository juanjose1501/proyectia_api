from pydantic import BaseModel

class ProyectoIn(BaseModel):
    nombre: str
    empresa: str
   

class ProyectoOut(BaseModel):
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
    