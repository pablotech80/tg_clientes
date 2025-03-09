from tg.configuration import AppConfig

from tg import TGController, expose
from tg_clientes.config.app_cfg import custom_config

import tg_clientes
import tg_clientes.model as model


class RootController(TGController):
    @expose()
    def index(self):
        return "¡TurboGears está funcionando correctamente!"


def make_app(global_conf, **app_conf):
    """Función de entrada para crear la aplicación TurboGears."""

    # Usar la configuración personalizada
    custom_config.root_controller = RootController()

    return custom_config.make_wsgi_app()
