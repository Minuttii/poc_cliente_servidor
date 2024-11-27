from setuptools import setup, find_packages

setup(
    name="poc_cliente_servidor",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "cliente = cliente.cliente:main",
            "servidor = servidor.servidor:main"
        ]
    },
)
