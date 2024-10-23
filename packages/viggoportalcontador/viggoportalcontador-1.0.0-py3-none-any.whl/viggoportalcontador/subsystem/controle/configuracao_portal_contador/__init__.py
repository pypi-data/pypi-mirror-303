from viggocore.common import subsystem
from viggoportalcontador.subsystem.controle.configuracao_portal_contador \
  import resource, manager, router

subsystem = subsystem.Subsystem(resource=resource.ConfiguracaoPortalContador,
                                manager=manager.Manager,
                                router=router.Router)
