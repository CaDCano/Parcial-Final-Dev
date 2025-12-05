from pydantic import BaseModel
from typing import Optional
from utils.positions import Position
from utils.resultado import Resultado
from utils.pie import PieDominante
from utils.states import States


class JugadorBase(BaseModel):
    nombre: str
    posicion: Position
    estado: States = States.ACTIVO
    dorsal: Optional[int] = None
    nacionalidad: Optional[str] = None
    altura: Optional[float] 
    peso: Optional[int]
    pie_Dominante: PieDominante
    anio_Nacimiento: Optional[int]

class JugadorCreate(JugadorBase):
    pass

class Jugador(JugadorBase):
    id: int
    class Config:
        orm_mode = True

class PartidoBase(BaseModel):
    rival: str
    fecha: Optional[str] = None
    local: Optional[str] = None
    resultado: Resultado

class PartidoCreate(PartidoBase):
    pass

class Partido(PartidoBase):
    id: int
    class Config:
        orm_mode = True

class EstadisticaBase(BaseModel):
    jugador_id: int
    partido_id: Optional[int] = None
    goles: int = 0
    asistencias: int = 0
    sanciones: int = 0

class EstadisticaCreate(EstadisticaBase):
    pass

class Estadistica(EstadisticaBase):
    id: int
    class Config:
        orm_mode = True
