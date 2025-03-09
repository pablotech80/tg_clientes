from setuptools import setup, find_packages

setup(
    name="tg_clientes",
    author="PABLO TECHERA",
    email="ptecherasosa@icloud.com",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "TurboGears2",
        "SQLAlchemy",
        "psycopg2",
        "Jinja2",
        "python-dotenv",
    ],
    entry_points={
        'paste.app_factory': [
            'main = tg_clientes.config.middleware:make_app',
        ],
    },
)
