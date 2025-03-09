from tg import expose, redirect, validate, flash
from tg.controllers import RestController
from tg.decorators import with_trailing_slash
from tg.validation import require
from sqlalchemy.exc import IntegrityError
from tg_clientes.model import DBSession, Cliente
from tg import predicates

class ClienteController(RestController):
    """Controlador para manejar el CRUD de clientes"""

    allow_only = predicates.has_permission('manage', msg="Debe estar autenticado para acceder.")

    @expose('tg_clientes.templates.clientes')
    def get_all(self):
        """Lista todos los clientes"""
        clientes = DBSession.query(Cliente).all()
        return dict(clientes=clientes)

    @expose('tg_clientes.templates.cliente_form')
    def new(self, **kw):
        """Muestra el formulario para crear un nuevo cliente"""
        return dict(cliente=None)

    @expose()
    def post(self, nombre, codigo, telefono1=None, direccion=None, nif=None):
        """Crea un nuevo cliente"""
        try:
            nuevo_cliente = Cliente(
                nombre=nombre, codigo=codigo, telefono1=telefono1, direccion=direccion, nif=nif
            )
            DBSession.add(nuevo_cliente)
            DBSession.flush()
            flash("Cliente creado correctamente", "success")
        except IntegrityError:
            flash("El código de cliente ya existe.", "error")
        return redirect('/clientes')

    @expose('tg_clientes.templates.cliente_form')
    def edit(self, id):
        """Muestra el formulario para editar un cliente existente"""
        cliente = DBSession.query(Cliente).get(id)
        return dict(cliente=cliente)

    @expose()
    def put(self, id, nombre, codigo, telefono1=None, direccion=None, nif=None):
        """Actualiza los datos de un cliente"""
        cliente = DBSession.query(Cliente).get(id)
        if cliente:
            cliente.nombre = nombre
            cliente.codigo = codigo
            cliente.telefono1 = telefono1
            cliente.direccion = direccion
            cliente.nif = nif
            DBSession.flush()
            flash("Cliente actualizado correctamente", "success")
        else:
            flash("Cliente no encontrado", "error")
        return redirect('/clientes')

    @expose('tg_clientes.templates.cliente_eliminar')
    def delete(self, id):
        """Muestra la confirmación para eliminar un cliente"""
        cliente = DBSession.query(Cliente).get(id)
        return dict(cliente=cliente)

    @expose()
    def post_delete(self, id):
        """Elimina un cliente"""
        cliente = DBSession.query(Cliente).get(id)
        if cliente:
            DBSession.delete(cliente)
            DBSession.flush()
            flash("Cliente eliminado correctamente", "success")
        else:
            flash("Cliente no encontrado", "error")
        return redirect('/clientes')
