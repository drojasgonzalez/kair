class Book:
    def __init__(self, book_id, title, authors, publisher, description):
        # Inicializa las propiedades básicas del libro.
        self.book_id = book_id
        self.title = title
        self.authors = authors
        self.publisher = publisher
        self.description = description

    @classmethod
    def from_api_data(cls, api_data):
        # Crea una instancia de Book a partir de datos de una API.
        volume_info = api_data.get('volumeInfo', {})
        return cls(
            book_id=api_data.get('id', ''),
            title=volume_info.get('title', ''),
            authors=', '.join(volume_info.get('authors', [])),
            publisher=volume_info.get('publisher', ''),
            description=volume_info.get('description', '')
        )

    def to_dict(self):
        # Convierte la instancia de Book a un diccionario para preparar datos a csv por cada libro.
        return {
            'id': self.book_id,
            'title': self.title,
            'authors': self.authors,
            'publisher': self.publisher,
            'description': self.description,
        }
