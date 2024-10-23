from viggocore.common.subsystem import operation, manager
from viggocore.common import exception
from viggoportalcontador.subsystem.controle\
    .configuracao_portal_contador.resource import (
        ConfiguracaoPortalContadorTipo as cpc_tipo)


class Create(operation.Create):

    def pre(self, session, **kwargs):
        tipo = kwargs.get('tipo', None)
        configuracao_portal_contadors = self.manager.list(tipo=tipo)
        if len(configuracao_portal_contadors) > 0:
            raise exception.BadRequest(
                f'Já existe uma configuração para o tipo {tipo}, '
                'por favor edite ela!')
        return super().pre(session, **kwargs)


class Update(operation.Update):

    def do(self, session, **kwargs):
        # remove o tipo do kwargs pois essa informação não é editável
        kwargs.pop('tipo', None)
        return super().do(session, **kwargs)


class Manager(manager.Manager):

    def __init__(self, driver):
        super(Manager, self).__init__(driver)
        self.create = Create(self)
        self.update = Update(self)

    def get_configuracao_portal_contador(
            self, tipo: cpc_tipo = cpc_tipo.PRODUCAO):
        configs = self.list(tipo=tipo.name)
        if len(configs) == 0:
            raise exception.BadRequest(
                'Nenhuma configuração do Portal Contador cadastrada para o ' +
                f'tipo {tipo.name}, por favor ' +
                'cadastre uma para usar a api.')
        return configs[0]
