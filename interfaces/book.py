class Book:
    def __init__(self, book_id, title, authors, publisher, description):
        self.book_id = book_id
        self.title = title
        self.authors = authors
        self.publisher = publisher
        self.description = description

    @classmethod
    def from_api_data(cls, api_data):
        volume_info = api_data.get('volumeInfo', {})
        return cls(
            book_id=api_data.get('id', ''),
            title=volume_info.get('title', ''),
            authors=', '.join(volume_info.get('authors', [])),
            publisher=volume_info.get('publisher', ''),
            description=volume_info.get('description', '')
        )

    def to_dict(self):
        return {
            'id': self.book_id,
            'title': self.title,
            'authors': self.authors,
            'publisher': self.publisher,
            'description': self.description,
        }
