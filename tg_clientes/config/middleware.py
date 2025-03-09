from tg.configuration.app_config import AppConfig
from tg import TGController, expose

import tg_clientes
import tg_clientes.model as model

class RootController(TGController):
    @expose()
    def index(self):
        return "¡TurboGears está funcionando correctamente!"

def make_app(global_conf, **app_conf):
    """Función de entrada para crear la aplicación TurboGears."""
    app_cfg = AppConfig(minimal=True, root_controller=RootController())

    # Aquí estaba el error
    app_cfg.package = tg_clientes  # Antes estaba mal apuntando a config.package

    return app_cfg.make_wsgi_app()
