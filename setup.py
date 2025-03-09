from setuptools import setup, find_packages

setup(
    name='tg_clientes',
    version='0.1',
    description='Aplicación TurboGears de gestión de clientes',
    author='Pablo Techera',
    author_email='ptechersosa@icloud.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "TurboGears2",
        "SQLAlchemy",
        "psycopg2",
        "PasteDeploy",
        "Jinja2",
        "alembic"
    ],
entry_points={
    'paste.app_factory': [
        'main = tg_clientes.config.middleware:make_app',
    ],
    'gearbox.command': [
        'setup-app = tg_clientes.websetup:init_setup',
    ],
},
)
