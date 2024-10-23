from viggocore.common import subsystem
from viggoportalcontador.subsystem.controle.portal_contador \
  import resource, controller, router, manager

subsystem = subsystem.Subsystem(resource=resource.PortalContador,
                                controller=controller.Controller,
                                manager=manager.Manager,
                                router=router.Router)
