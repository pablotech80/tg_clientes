

from tg import config
import tg_clientes.model as model


def setup_app(command, conf, vars):
	"""Configura la base de datos e inicializa la aplicación."""
	print("Configurando la base de datos...")

	# Conectar con la base de datos configurada en `development.ini`
	engine = model.DBSession.bind
	model.metadata.create_all(engine)

	# Agregar datos iniciales si es necesario
	print("Base de datos creada correctamente.")
