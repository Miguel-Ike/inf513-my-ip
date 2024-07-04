import requests

def get_public_ip():
    """Obtiene la dirección IP pública"""
    try:
        response = requests.get("http://ipinfo.io/ip")
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP 4xx/5xx
        return response.text.strip()
    except requests.RequestException as e:
        raise ConnectionError("No se puede obtener la dirección IP pública. Verifique su conexión a Internet.") from e
