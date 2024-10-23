from enum import Enum

import sqlalchemy

from viggocore.common.subsystem import entity
from viggocore.database import db


class ConfiguracaoPortalContadorTipo(Enum):
    HOMOLOGACAO = 'HOMOLOGACAO'
    PRODUCAO = 'PRODUCAO'


class ConfiguracaoPortalContador(entity.Entity, db.Model):

    attributes = ['tipo', 'email', 'senha']
    attributes += entity.Entity.attributes

    tipo = db.Column(sqlalchemy.Enum(ConfiguracaoPortalContadorTipo),
                     nullable=False)
    email = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    authorization = db.Column(db.String(1000), nullable=True)

    def __init__(self, id, tipo, email, senha, authorization=None,
                 active=True, created_at=None, created_by=None,
                 updated_at=None, updated_by=None, tag=None):
        super().__init__(id, active, created_at, created_by,
                         updated_at, updated_by, tag)
        self.tipo = tipo
        self.email = email
        self.senha = senha
        self.authorization = authorization

    @classmethod
    def individual(self):
        return 'configuracao_portal_contador'

    @classmethod
    def collection(self):
        return 'configuracao_portal_contadores'
