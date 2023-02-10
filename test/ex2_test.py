# TO MAKE TESTS 
import unittest
import logging

# TO IMPORT TEST FILE
import sys 
sys.path.append('')

# TO test 
from ex2 import Book , Library, Client

class TestBook(unittest.TestCase):

    def setUp(self):
        self.book = Book("To Kill a Mockingbird", "Harper Lee")

    def test_check_out(self):
        self.book.check_out()
        self.assertTrue(self.book.is_checked_out)
        self.assertEqual(f"{self.book.title} by {self.book.author} has been checked out.", "To Kill a Mockingbird by Harper Lee has been checked out.")

    def test_check_in(self):
        self.book.check_out()
        self.book.check_in()
        self.assertFalse(self.book.is_checked_out)
        self.assertEqual(f"{self.book.title} by {self.book.author} has been checked in.", "To Kill a Mockingbird by Harper Lee has been checked in.")

class TestClient(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.book1 = Book("To Kill a Mockingbird", "Harper Lee")
        self.library.add_book(self.book1)
        self.book2 = Book("Pride and Prejudice", "Jane Austen")
        self.library.add_book(self.book2)
        self.client = Client("John Doe")

    def test_check_out_book(self):
        # Test check_out_book for valid input
        self.client.check_out_book(self.library, "To Kill a Mockingbird")
        self.assertTrue(self.book1.is_checked_out)
        self.assertIn(self.book1, self.client.checked_out_books)
        
        # Test check_out_book for not available book
        try:
            self.client.check_out_book(self.library, "Not a Book")
        except Exception as e:
            self.assertEqual(str(e), "Sorry, Not a Book is not available.")

    def test_check_in_book(self):
        # Test check_in_book for valid input
        self.client.check_out_book(self.library, "To Kill a Mockingbird")
        self.client.check_in_book(self.library, "To Kill a Mockingbird")
        self.assertFalse(self.book1.is_checked_out)
        self.assertNotIn(self.book1, self.client.checked_out_books)
        
        # Test check_in_book for not checked out book
        with self.assertRaises(Exception) as context:
            self.client.check_in_book(self.library, "Pride and Prejudice")
            self.assertEqual(str(context.exception), "Sorry, Pride and Prejudice is not checked out.")

class TestLibraryMethods(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.book1 = Book("To Kill a Mockingbird", "Harper Lee")
        self.library.add_book(self.book1)
        self.book2 = Book("Pride and Prejudice", "Jane Austen")
        self.library.add_book(self.book2)

    def test_add_book(self):
        self.assertIn(self.book1, self.library.books)
        self.assertIn(self.book2, self.library.books)
        self.assertEqual(f"{self.book1.title} by {self.book1.author} has been added to the library.", 
                        "To Kill a Mockingbird by Harper Lee has been added to the library.")
        self.assertEqual(f"{self.book2.title} by {self.book2.author} has been added to the library.", 
                        "Pride and Prejudice by Jane Austen has been added to the library.")

    def test_check_out_book(self):
        self.library.check_out_book("To Kill a Mockingbird")
        self.assertTrue(self.book1.is_checked_out)
        self.library.check_out_book("Pride and Prejudice")
        self.assertTrue(self.book2.is_checked_out)

    def test_check_in_book(self):
        self.library.check_out_book("To Kill a Mockingbird")
        self.library.check_out_book("Pride and Prejudice")
        self.library.check_in_book("To Kill a Mockingbird")
        self.assertFalse(self.book1.is_checked_out)
        self.library.check_in_book("Pride and Prejudice")
        self.assertFalse(self.book2.is_checked_out)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr)
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()