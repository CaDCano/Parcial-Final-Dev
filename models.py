import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum as SAEnum
from sqlalchemy.orm import relationship
from database import Base
from utils.positions import Position
from utils.states import States
from utils.pie import PieDominante
from utils.resultado import Resultado
class Jugador(Base):
    __tablename__ = "jugadores"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    posicion = Column(SAEnum(Position), nullable=False)
    estado = Column(SAEnum(States), nullable=False, default=States.ACTIVO)
    dorsal = Column(Integer, nullable=True)
    nacionalidad = Column(String, nullable=True)
    altura = Column(float, nullable=True)
    peso = Column(Integer,nullable=True)
    pie_Dominante = Column(SAEnum(PieDominante),nullable=False)
    anio_Nacimiento = Column(Integer, nullable=True)

    estadisticas = relationship("Estadistica", back_populates="jugador")


class Estadistica(Base):
    __tablename__ = "estadisticas"
    id = Column(Integer, primary_key=True, index=True)
    jugador_id = Column(Integer, ForeignKey("jugadores.id"))
    partido_id = Column(Integer, ForeignKey("partidos.id"), nullable=True)
    goles = Column(Integer, default=0)
    asistencias = Column(Integer, default=0)
    sanciones = Column(Integer, default=0)

    jugador = relationship("Jugador", back_populates="estadisticas")
class Club(Base):# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA <--- FALTA
    pass


class Partido(Base):
    __tablename__ = "partidos"
    id = Column(Integer, primary_key=True, index=True)
    rival = Column(String, nullable=False)
    fecha = Column(DateTime, default=datetime.datetime.utcnow)
    local = Column(String, nullable=True)
    resultado = Column(SAEnum(Resultado), nullable=True)



