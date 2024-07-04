from datetime import datetime

def get_greeting(language):
    """Genera un saludo basado en la hora del día y el idioma"""
    current_hour = datetime.now().hour
    if language == 'es':
        if 4 <= current_hour < 12:
            return "Buenos días"
        elif 12 <= current_hour < 18:
            return "Buenas tardes"
        else:
            return "Buenas noches"
    elif language == 'fr':
        if 4 <= current_hour < 12:
            return "Bonjour"
        elif 12 <= current_hour < 18:
            return "Bon après-midi"
        else:
            return "Bonsoir"
    elif language == 'en':
        if 4 <= current_hour < 12:
            return "Good morning"
        elif 12 <= current_hour < 18:
            return "Good afternoon"
        else:
            return "Good evening"
    else:
        raise ValueError("Idioma no soportado. Por favor elija entre 'es', 'fr', o 'en'.")
