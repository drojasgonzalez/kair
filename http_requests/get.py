import os
from dotenv import load_dotenv
import requests

# Carga las variables de entorno desde .env.local
load_dotenv(dotenv_path='.env.local')

def fetch_books_data(search_term):
    
    api_url = os.getenv('GOOGLE_BOOKS_API_URL')
    url = f'{api_url}?q={search_term}'
    
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

results = fetch_books_data('search+terms')
#print(results)
