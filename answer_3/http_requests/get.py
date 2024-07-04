# Importamos los módulos necesarios
import os  
import requests
from dotenv import load_dotenv  

load_dotenv(dotenv_path='.env.local')

def fetch_user_data():    
    api_url = os.getenv('API_URL') + 'users'

    response = requests.get(api_url)
    
    if response.status_code == 200:
        return response.json()  # responde en JSON
    else:
        response.raise_for_status()  # excepción si no es 200


def fetch_post_data():    
    api_url = os.getenv('API_URL') + 'posts'

    response = requests.get(api_url)
    
    if response.status_code == 200:
        return response.json()  # responde en JSON
    else:
        response.raise_for_status()  # excepción si no es 200


