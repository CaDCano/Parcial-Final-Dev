from sqlalchemy.orm import Session
import models, schemas
from utils.positions import Position
from utils.states import States
from utils.pie import PieDominante
from utils.resultado import Resultado

# Jugadores
def get_jugadores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Jugador).offset(skip).limit(limit).all()

def get_jugador(db: Session, jugador_id: int):
    return db.query(models.Jugador).filter(models.Jugador.id == jugador_id).first()

def create_jugador(db: Session, jugador: schemas.JugadorCreate):
    db_j = models.Jugador(
        nombre=jugador.nombre,
        posicion=jugador.posicion, #Enum
        estado=jugador.estado, #Enum
        dorsal=jugador.dorsal,
        nacionalidad=jugador.nacionalidad,
        altura = jugador.altura,
        peso = jugador.peso,
        pie_Dominante =  jugador.pie_Dominante, #Enum
        anio_Nacimineto = jugador.anio_Nacimiento
    )
    db.add(db_j)
    db.commit()
    db.refresh(db_j)
    return db_j

def update_jugador(db: Session, jugador_id: int, data: dict):
    j = db.query(models.Jugador).filter(models.Jugador.id == jugador_id).first()
    if not j:
        return None
    for k, v in data.items():
        setattr(j, k, v)
    db.commit()
    db.refresh(j)
    return j

def delete_jugador(db: Session, jugador_id: int):
    j = db.query(models.Jugador).filter(models.Jugador.id == jugador_id).first()
    if not j:
        return False
    db.delete(j)
    db.commit()
    return True

# Partidos
def get_partidos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Partido).offset(skip).limit(limit).all()

def create_partido(db: Session, partido: schemas.PartidoCreate):
    p = models.Partido(**partido.dict())
    db.add(p)
    db.commit()
    db.refresh(p)
    return p

# Estadisticas
def get_estadisticas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Estadistica).offset(skip).limit(limit).all()

def create_estadistica(db: Session, estad: schemas.EstadisticaCreate):
    db_e = models.Estadistica(**estad.dict())
    db.add(db_e)
    db.commit()
    db.refresh(db_e)
    return db_e
