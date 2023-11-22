from flask_sqlalchemy import SQLAlchemy
from database import db

class Personalizacion(db.Model):
    __tablename__ = 'personalizacion'
    id_p = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    color = db.Column(db.String(255), nullable=False)
    tipo = db.Column(db.String(255), nullable=False)
    lente = db.Column(db.String(255), nullable=False)
    urlfo = db.Column(db.String(255), nullable=False)
    id_u = db.Column(db.Integer, nullable=False)

    def __init__(self, color, tipo, lente, urlfo, id_u):
        self.color = color
        self.tipo = tipo
        self.lente = lente
        self.urlfo = urlfo
        self.id_u = id_u

    def __repr__(self):
        return f'<Personalizacion {self.id_p}>'
