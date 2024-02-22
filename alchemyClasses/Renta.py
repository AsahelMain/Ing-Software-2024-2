from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from alchemyClasses import db
from alchemyClasses.Usuario import Usuario
from alchemyClasses.Pelicula import Pelicula

class Renta(db.Model):
    __tablename__ = 'rentar'
    idRentar = Column(Integer, primary_key=True)
    idUsuario = Column(Integer, ForeignKey(Usuario.idUsuario))
    idPelicula = Column(Integer, ForeignKey(Pelicula.idPelicula))
    fecha_renta = Column(DateTime)
    dias_de_renta = Column(Integer, default=5)
    estatus = Column(Boolean, default=0)

    def __init__(self,idUsuario,idPelicula,fecha_renta,dias_de_renta=5,estatus=0):
        self.idUsuario = idUsuario
        self.idPelicula = idPelicula
        self.fecha_renta = fecha_renta
        self.dias_de_renta = dias_de_renta
        self.estatus = estatus

    def __str__(self):
        return f'ID-usuario: {self.idUsuario}\nID-Pelicula: {self.idPelicula}\nFecha de la renta: {self.fecha_renta}'


