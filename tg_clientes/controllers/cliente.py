from tg import expose, redirect, session
from tg.controllers import TGController

class ClienteController(TGController):
    @expose('tg_clientes.templates.clientes')  # Asegurar que devuelve una plantilla
    def index(self):
        """Lista de Clientes - Solo accesible si el usuario está autenticado"""
        if 'user' not in session:
            redirect('/auth/login')
        return dict(clientes=["Cliente 1", "Cliente 2", "Cliente 3"])  # Datos de prueba

    @expose()
    def nuevo(self):
        """Formulario de creación de cliente"""
        if 'user' not in session:
            redirect('/auth/login')
        return "Formulario para crear cliente."

    @expose()
    def editar(self, id):
        """Edición de un cliente"""
        if 'user' not in session:
            redirect('/auth/login')
        return f"Editando cliente con ID: {id}"

    @expose()
    def eliminar(self, id):
        """Eliminar cliente"""
        if 'user' not in session:
            redirect('/auth/login')
        return f"Eliminando cliente con ID: {id}"
