import os
import viggocore

from viggocore.system import System
from flask_cors import CORS
from viggoportalcontador.subsystem.controle \
    import portal_contador, configuracao_portal_contador
from viggoportalcontador.resources import SYSADMIN_EXCLUSIVE_POLICIES, \
    SYSADMIN_RESOURCES, USER_RESOURCES


system = System('viggoportalcontador',
                [portal_contador.subsystem,
                 configuracao_portal_contador.subsystem],
                USER_RESOURCES,
                SYSADMIN_RESOURCES,
                SYSADMIN_EXCLUSIVE_POLICIES)


class SystemFlask(viggocore.SystemFlask):

    def __init__(self):
        super().__init__(system)

    def configure(self):
        origins_urls = os.environ.get('ORIGINS_URLS', '*')
        CORS(self, resources={r'/*': {'origins': origins_urls}})

        self.config['BASEDIR'] = os.path.abspath(os.path.dirname(__file__))
        self.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        viggoportalcontador_database_uri = os.getenv(
            'VIGGOPORTALCONTADOR_DATABASE_URI', None)
        if viggoportalcontador_database_uri is None:
            raise Exception(
                'VIGGOPORTALCONTADOR_DATABASE_URI not defined in enviroment.')
        else:
            # URL os enviroment example for Postgres
            # export VIGGOPORTALCONTADOR_DATABASE_URI=
            # mysql+pymysql://root:mysql@localhost:3306/viggoportalcontador
            self.config['SQLALCHEMY_DATABASE_URI'] = (
                viggoportalcontador_database_uri)
