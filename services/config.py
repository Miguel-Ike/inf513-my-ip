import os

def get_env_variable(name):
    """Obtiene una variable de entorno y verifica que no sea None"""
    value = os.getenv(name)
    if value is None:
        raise ValueError(f"La variable de entorno {name} no está definida")
    return value
