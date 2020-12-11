from typing import Dict
from pydantic import BaseModel

class EmpresaInDB(BaseModel):
    nombre: str
    email: str
    contraseña: str
    pais: str
    NIT: str
    ciudad: str
    telefono: str
    direccion: str
    num_empleados : int
    keyword: str

database_empresa = Dict[str, EmpresaInDB]
database_empresa = {
    "cartonlopez@gmail.com": EmpresaInDB(**{"nombre":"Cartones Lopez",
                                "email":"cartonlopez@gmail.com",
                                "contraseña":"reciclaje",
                                "pais":"Colombia",
                                "NIT":"123.456.789",
                                "ciudad":"Cali",
                                "telefono":"3453434",
                                "direccion":"Cra 75 DA # 2 Sur",
                                "num_empleados":9,
                                "keyword":"pizza" }),
    "gerenciaArtCafe@yahoo.com": EmpresaInDB(**{"nombre":"Artesanos Cafeteros",
                                "email":"gerenciaArtCafe@yahoo.com",
                                "contraseña":"aromadecafe",
                                "pais":"Colombia",
                                "NIT":"168.235.213",
                                "ciudad":"Armenia",
                                "telefono":"3221485",
                                "direccion":"Calle 6 Sur # 50 EE",
                                "num_empleados": 8,
                                "keyword":"cafe" }),
    "JuanJose": EmpresaInDB(**{"nombre":"Metric Software",
                                "email":"metricsoftware2@gmail.com",
                                "contraseña":"holamundo",
                                "pais":"Colombia",
                                "NIT":"119.287.154",
                                "ciudad":"Cartagena",
                                "telefono":"2563788",
                                "direccion":"Cra 43B 120",
                                "num_empleados":6,
                                "keyword":"python" })
}
