import os
from dotenv import load_dotenv
from services.config import get_env_variable
from services.ip_service import get_public_ip
from services.message_service import create_custom_message

# Cargar variables del archivo .env específico
load_dotenv(dotenv_path='.env')

def main():
    group = get_env_variable('GROUP')
    full_name = get_env_variable('FULL_NAME')
    teacher = get_env_variable('TEACHER')
    
    try:
        ip = get_public_ip()
        # Crear y mostrar mensajes en los tres idiomas
        message_es = create_custom_message(ip, group, full_name, teacher, 'es')
        message_fr = create_custom_message(ip, group, full_name, teacher, 'fr')
        message_en = create_custom_message(ip, group, full_name, teacher, 'en')

        print("\n[ Mensaje en Español ]")
        print(message_es)

        print("\n[ Message en Français ]")
        print(message_fr)

        print("\n[ Message in English ]")
        print(message_en)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
