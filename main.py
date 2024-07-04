from http_requests.get import fetch_books_data  # API Layer 
from interfaces.book import Book  # Clase Books | interface layer 
from helpers.export_csv import save_to_csv  # Helper para exportar datos a csv  | middleware layer 

def main():
    search_term = 'search+terms' # La api necesita estos parámetros obligatorios 
    books_data = fetch_books_data(search_term) #APi use 
    
    # 'items' existe en la respuesta de la API 
    if 'items' in books_data:
        print(f"Total items: {books_data['totalItems']}")
        
        # Lista almacena libros que están en  diccionarios
        books_list = []

        for item in books_data['items']:
            # Crear una instancia de Book utilizando los datos de la API
            book = Book.from_api_data(item)
            # Convertir el libro a un diccionario y añadirlo a la lista de libros
            books_list.append(book.to_dict())
        
        # Pasar lista de libros a método csv
        save_to_csv(books_list)
    else:
        print("No se encontraron libros.")

# Entrada principal del programa: ejecutar la función main si este script es el punto de entrada
if __name__ == '__main__':
    main()
