import json
import requests
from viggocore.common.subsystem import operation, manager
from viggocore.common import exception
from viggoportalcontador.subsystem.controle.configuracao_portal_contador\
    .resource import ConfiguracaoPortalContadorTipo as cpc_tipo


class EnviarNfeString(operation.Create):

    def pre(self, session, **kwargs):
        return True

    def do(self, session, **kwargs):
        ambiente = kwargs.pop('api_fiscal', None)
        cpf_cnpj = kwargs.pop('cpf_cnpj', None)
        url = f'/NFeString/{cpf_cnpj}/1'
        return self.manager.executar_requisicao(
            'POST', url, json=kwargs, ambiente=ambiente)


class CancelarNfeString(operation.Create):

    def do(self, session, **kwargs):
        ambiente = kwargs.pop('api_fiscal', None)
        modelo_nota = kwargs.pop('modelo_nota', None)
        url = f'/CancelarNFeString/{modelo_nota}'
        return self.manager.executar_requisicao(
            'POST', url, json=kwargs, ambiente=ambiente)


class Manager(manager.Manager):
    BASE_URL_PROD = 'http://fiscal.viggosistemas.com.br/api/v1'
    BASE_URL_HOMO = 'http://fiscal-hom.viggosistemas.com.br/api/v1'

    def __init__(self, driver):
        super(Manager, self).__init__(driver)
        # rotas de empresa
        self.enviar_nfe_string = EnviarNfeString(self)
        self.cancelar_nfe_string = CancelarNfeString(self)

    def get_authorization(self, ambiente: cpc_tipo = None):
        config = self.api.configuracao_portal_contadors().\
            get_configuracao_portal_contador(tipo=ambiente)
        data = {'Authorization': config.authorization}

        if config.authorization is None or len(config.authorization) == 0:
            url = self.get_endpoint('/login', ambiente)
            body = {
                'email': config.email,
                'senha': config.senha
            }

            headers = {'Content-Type': 'application/json'}

            response = requests.post(url, data=body, headers=headers)

            if response.status_code == 200:
                response = self.montar_response_dict(response)
                data['Authorization'] = 'Bearer ' + response.get('token', '')
                self.api.configuracao_portal_contadors().update(
                    id=config.id, **{'authorization': data['Authorization']})
            else:
                raise exception.BadRequest(
                    'Não foi possível gerar a autorização.')
        return data

    def get_cpf_cnpj(self, **kwargs):
        cpf_cnpj = kwargs.get('cpf_cnpj', None)
        if cpf_cnpj is None:
            raise exception.BadRequest('O campo cpf_cnpj é obrigatório.')
        return cpf_cnpj

    def get_endpoint(self, resource, ambiente=None):
        urls = {
            cpc_tipo.HOMOLOGACAO: self.BASE_URL_HOMO + resource,
            cpc_tipo.PRODUCAO: self.BASE_URL_PROD + resource}
        return urls.get(ambiente, '')

    def executar_requisicao(self, method, endpoint, ambiente,
                            params={}, json={},
                            headers={'Content-Type': 'application/json'},
                            data={}, sem_authorization=True):

        # completa o endpoint com a url passada
        endpoint = self.get_endpoint(endpoint, ambiente)

        if sem_authorization is True:
            headers.update(self.get_authorization(ambiente=ambiente))

        if method == 'GET':
            return requests.get(
                endpoint, params=params, json=json, headers=headers, data=data)
        elif method == 'POST':
            return requests.post(
                endpoint, params=params, json=json, headers=headers, data=data)
        elif method == 'PUT':
            return requests.put(
                endpoint, params=params, json=json, headers=headers, data=data)
        elif method == 'DELETE':
            return requests.delete(endpoint)
        else:
            raise exception.OperationBadRequest(
                'Método de requisição não permitido.')

    def montar_response_dict(self, response):
        try:
            response_dict = json.loads(response.text)
        except Exception:
            response_dict = {'error': response.text}
        return response_dict
