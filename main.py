import csv
from http_requests.get import fetch_books_data
from interfaces.book import Book

def save_to_csv(data, filename='books.csv'):
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

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
