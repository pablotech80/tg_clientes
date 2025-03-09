from tg_clientes.controllers.cliente import ClienteController

class RootController(BaseController):
    clientes = ClienteController()
