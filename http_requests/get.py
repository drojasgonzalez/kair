# Importamos los módulos necesarios
import os  
from dotenv import load_dotenv  
import requests

load_dotenv(dotenv_path='.env.local')

def fetch_books_data(search_term):    
        
    # Obtiene la URL de la API de Google Books desde las variables de entorno
    api_url = os.getenv('GOOGLE_BOOKS_API_URL')
    # Construye la URL completa con el término de búsqueda proporcionado
    url = f'{api_url}?q={search_term}'
    
    # Realiza una solicitud GET a la API
    response = requests.get(url)
    
    
    if response.status_code == 200:
        return response.json()  # responde en JSON
    else:
        response.raise_for_status()  # excepción si no es 200

# results = fetch_books_data('search+terms')
# print(results) 
