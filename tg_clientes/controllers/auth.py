from tg import expose, request, redirect, session
from tg.controllers import TGController
import os
import html
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

class AuthController(TGController):
    @expose('tg_clientes.templates.login')
    def login(self, came_from='/'):
        """Muestra el formulario de login"""
        return dict(came_from=came_from)

    @expose()
    def authenticate(self, username, password):
        """Verifica las credenciales del usuario"""
        username = html.escape(username.strip())
        password = html.escape(password.strip())

        admin_username = os.getenv("ADMIN_USERNAME", "admin")
        admin_password = os.getenv("ADMIN_PASSWORD", "admin")

        print(f"Usuario ingresado: {username}")  # 👀 Debug
        print(f"Contraseña ingresada: {password}")
        print(f"Usuario esperado: {admin_username}")
        print(f"Contraseña esperada: {admin_password}")

        if username == admin_username and password == admin_password:
            print("✅ Autenticación exitosa")  # 👀 Debug
            session['user'] = username  # Guardar en la sesión
            session.save()
            print(f"Sesión guardada: {session}")  # 👀 Debug
            redirect('/clientes')  # Redirigir al CRUD
        else:
            print("❌ Autenticación fallida")  # 👀 Debug
            redirect('/auth/login?error=1')

    @expose()
    def logout(self):
        """Cierra sesión y redirige al login"""
        session.pop('user', None)
        session.save()
        print("🛑 Sesión cerrada")  # 👀 Debug
        redirect('/auth/login')
