from tg import expose, redirect, session
from tg.controllers import TGController
from tg_clientes.controllers.auth import AuthController
from tg_clientes.controllers.cliente import ClienteController


class RootController(TGController):
    auth = AuthController()  # Asegurar que esté bien definido
    clientes = ClienteController()
    @expose()
    def index(self):
        """Redirigir al login si no hay usuario en sesión"""
        if 'user' not in session:
            redirect('/auth/login')
        return "Bienvenido a la gestión de clientes"
