import flask

from viggocore.common import exception, utils, controller


class Controller(controller.CommonController):

    def __init__(self, manager, resource_wrap, collection_wrap):
        super(Controller, self).__init__(
            manager, resource_wrap, collection_wrap)

    def enviar_nfe_string(self):
        data = flask.request.get_json()
        try:
            response = self.manager.enviar_nfe_string(**data)
        except exception.ViggoCoreException as exc:
            return flask.Response(response=exc.message,
                                  status=exc.status)

        return flask.Response(response=utils.to_json(response),
                              status=response.status_code,
                              mimetype="text/plain")

    def cancelar_nfe_string(self):
        data = flask.request.get_json()
        try:
            response = self.manager.cancelar_nfe_string(**data)
        except exception.ViggoCoreException as exc:
            return flask.Response(response=exc.message,
                                  status=exc.status)

        return flask.Response(response=utils.to_json(response),
                              status=response.status_code,
                              mimetype="text/plain")
