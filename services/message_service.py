from services.greeting_service import get_greeting

def create_custom_message(ip, group, full_name, teacher, language):
    """Crea un mensaje personalizado usando el saludo y la dirección IP en el idioma seleccionado"""
    saludo = get_greeting(language)
    
    if language == 'fr':
        message = f"""
{saludo} Prof. {teacher},
Veuillez mettre à jour mon IP.

Groupe: {group}

{ip}
{full_name}
"""
    elif language == 'es':
        message = f"""
{saludo} Ing. {teacher},
Por favor, podría actualizar mi IP.

Grupo: {group}

{ip}
{full_name}
"""
    elif language == 'en':
        message = f"""
{saludo} Prof. {teacher},
Please update my IP.

Group: {group}

{ip}
{full_name}
"""
    else:
        raise ValueError("Idioma no soportado. Por favor elija entre 'es', 'fr', o 'en'.")
    
    return message
