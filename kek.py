class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Вывод: {self.title} by {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return True
        return False

    def list_books(self):
        return self.books

library = Library()
book1 = Book("1984", "George Orwell")
library.add_book(book1)
print(library.list_books())
library.remove_book("1984")
