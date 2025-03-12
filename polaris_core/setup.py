from setuptools import setup, find_packages

setup(
    name="polaris_core",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "SQLAlchemy",
        "TurboGears2",
        "psycopg2",
        "Alembic"
    ],
    include_package_data=True,
    description="Paquete local polaris_core",
)
