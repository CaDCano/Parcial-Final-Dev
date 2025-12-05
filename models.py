from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Jugador():
    __tablename__ = "jugadores"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    posicion = Column(SAEnum(Position), nullable=False)
    estado = Column(SAEnum(States), nullable=False, default=States.ACTIVO)
    dorsal = Column(Integer, nullable=True)
    nacionalidad = Column(String, nullable=True)

    estadisticas = relationship("Estadistica", back_populates="jugador")

    pass


class Estadistica():
    pass


class Partido():
    pass


