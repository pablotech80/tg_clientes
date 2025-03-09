from tg import TGController, expose, redirect, session
from tg_clientes.controllers.auth import AuthController
from tg_clientes.controllers.cliente import ClienteController

class RootController(TGController):
    auth = AuthController()
    clientes = ClienteController()

    @expose()
    def index(self):
        """Redirigir al login si no hay usuario en sesión"""
        if 'user' not in session:
            redirect('/auth/login')
        return "Bienvenido a la gestión de clientes"


print("Rutas disponibles en RootController:")
for attr in dir(RootController):
    if not attr.startswith("_"):
        print(f"/{attr}")
