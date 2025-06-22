class Book:
    def __init__(self, title: str, author: str, year: int):
        """Constructor to initialize the book's title, author, and publication year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor to print a message when the book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation of the book, suitable for recreating the instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the str method
    print(my_book)  # Expected to use str

    # Demonstrating the repr method
    print(repr(my_book))  # Expected to use repr

    # Deleting a book instance to trigger del
    del my_book

if __name__ == "__main__":
    main()
