import os
from dotenv import load_dotenv
from tg.configuration import AppConfig
import tg_clientes
import tg_clientes.model as model

# Cargar variables de entorno
load_dotenv()

class CustomAppConfig(AppConfig):
    def __init__(self):
        super().__init__(minimal=True, root_controller=None)  # Evitamos importar RootController aquí

        # Asignar el paquete de la aplicación
        self.package = tg_clientes
        self.model = model  # Conectar la base de datos

        # Configuración de sesiones
        self.sa_auth.cookie_secret = os.getenv("SESSION_SECRET", "super_secret_key")
        self.beaker = {
            'session.type': os.getenv("SESSION_TYPE", "file"),
            'session.data_dir': os.getenv("SESSION_DIR", "data/sessions"),
            'session.key': "tg_session",
            'session.secret': os.getenv("SESSION_SECRET", "super_secret_key"),
        }

# Crear una instancia de configuración
custom_config = CustomAppConfig()

# Aquí importamos RootController después de que `custom_config` está definido
from tg_clientes.controllers.root import RootController
custom_config.root_controller = RootController()  # Ahora sí lo asignamos
