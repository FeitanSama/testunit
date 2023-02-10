# Adds :
# - self in parameters of all functions
# - check if x or x and y are instance of numbers
# - error message if x or x and y are not instance of numbers
# - add documenation
# - delete 'tests' function in the end of script

class Book:

    """ A class for book

    Parameters
    __________

    title : string 
        title of the book

    author : string
        author of the book

    is_checked_out : boolean
        know if the book is checked out

    Methods
    __________

    __init__(title,author)
        init a book whith is title and author name    
    
    check_out()
        mark arg check_out as True

    check_in()
        mark arg check_out as False
    """

    def __init__(self, title, author):

        """ Function for init a book by his title and author name
        
        Parameters 
        __________

        title : string
            title of the book

        author : string
            author of the book

        is_checked_out : boolean
            false by default

        Returns
        __________

        None

        Raises
        __________

        None
        """
        self.title = title
        self.author = author
        self.is_checked_out = False

    def check_out(self):

        """ Function set the book status to check_out

            is_checked_out --> True

        Parameters
        __________

        None

        Returns
        __________

        None

        Raises
        __________

        None
        """

        self.is_checked_out = True
        print(f"{self.title} by {self.author} has been checked out.")

    def check_in(self):
        """ Function set the book status to check_out
        
            is_checked_out --> False

        Parameters
        __________

        None

        Returns
        __________

        None

        Raises
        __________

        None
        """
        self.is_checked_out = False
        print(f"{self.title} by {self.author} has been checked in.")

class Library:

    """ A class for library containing books information

    Parameters
    __________

    books : list
        contains all books informations

    Methods
    __________

    __init__(books)
        init empty list books in library  
    
    add_book()
        add a book to library

    check_out_book()
        search if a book was checked out by his title

    check_in_book()
        search if a book was checked in by his title
    """

    def __init__(self):
        """ Function to init a library

        Parameters
        __________

        None

        Returns
        __________

        None

        Raises
        __________

        None
        """
        self.books = []

    def add_book(self, book):
        """ Function to add a book to library

        Parameters
        __________

        book : object
            title and author

        Returns
        __________

        None

        Raises
        __________

        None
        """
        self.books.append(book)
        print(f"{book.title} by {book.author} has been added to the library.")

    def check_out_book(self, title):
        """ Function for check if a book is check_out

        Parameters
        __________

        title : object
            title of the book

        Returns
        __________

        None

        Raises
        __________

        None
        """
        for book in self.books:
            if book.title == title and not book.is_checked_out:
                book.check_out()
                return
        print(f"Sorry, {title} is not available.")

    def check_in_book(self, title):
        """ Function for check if a book is check_in

        Parameters
        __________

        title : object
            title of the book

        Returns
        __________

        None

        Raises
        __________

        None
        """
        for book in self.books:
            if book.title == title and book.is_checked_out:
                book.check_in()
                return
        print(f"Sorry, {title} is not in the library.")

class Client:

    """ A class for Client

    Parameters
    __________

    name : string
        name of the client

    Methods
    __________

    __init__(name)
        init name and check_out_book

    check_out_book(library, title)
        list check_out_book of the current client

    check_in_book(library, title)
        list check_in_book of the current client
    """
    def __init__(self, name):
        """ Function for init a client

        Parameters
        __________

        name : object
            name of the client

        Returns
        __________

        None

        Raises
        __________

        None
        """
        self.name = name
        self.checked_out_books = []

    def check_out_book(self, library, title):
        """ Function for check if a client 

        Parameters
        __________

        title : object
            title of the book

        Returns
        __________

        None

        Raises
        __________

        None
        """
        for book in library.books:
            if book.title == title and not book.is_checked_out:
                book.check_out()
                self.checked_out_books.append(book)
                return
        print(f"Sorry, {title} is not available.")

    def check_in_book(self, library, title):
        for book in self.checked_out_books:
            if book.title == title:
                book.check_in()
                self.checked_out_books.remove(book)
                return
        print(f"Sorry, {title} is not checked out.")

# Ajout de la ligne si dessous pour éviter d'éxécuter le code en important dans le fichier de test 
if __name__ == "__main__":
    library = Library()
    book1 = Book("To Kill a Mockingbird", "Harper Lee")
    library.add_book(book1)
    book2 = Book("Pride and Prejudice", "Jane Austen")
    library.add_book(book2)
    client1 = Client("John Doe")
    client1.check_out_book(library, "To Kill a Mockingbird")
    client1.check_out_book(library, "Pride and Prejudice")
    client2 = Client("Jane Doe")
    client2.check_out_book(library, "To Kill a Mockingbird")
    client1.check_in_book(library, "To Kill a Mockingbird")
