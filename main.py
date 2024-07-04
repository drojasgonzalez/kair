from http_requests.get import fetch_books_data
from interfaces.book import Book
from helpers.export_csv import save_to_csv

def main():
    search_term = 'search+terms'
    books_data = fetch_books_data(search_term)
    
    if 'items' in books_data:
        print(f"Total items: {books_data['totalItems']}")
        
        books_list = []
        for item in books_data['items']:
            book = Book.from_api_data(item)
            books_list.append(book.to_dict())
        
        save_to_csv(books_list)
    else:
        print("No se encontraron libros.")

if __name__ == '__main__':
    main()
