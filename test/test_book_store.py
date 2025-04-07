import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from io import StringIO
from unittest.mock import patch
from book_store import Book, BookStore


class TestBookStore(unittest.TestCase):
    def setUp(self):
        self.store = BookStore()
        self.book1 = Book("Title A", "Author A", 10.99, 5)
        self.book2 = Book("Title B", "Author B", 15.99, 3)
        self.store.add_book(self.book1)
        self.store.add_book(self.book2)

    def test_add_book(self):
        self.assertEqual(len(self.store.books), 2)
        self.assertEqual(self.store.books[0].title, "Title A")
        self.assertEqual(self.store.books[1].title, "Title B")

    def test_search_existing_book(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.store.search_book("Title A")
            self.assertIn("Found 1 book(s) with title 'Title A'", fake_out.getvalue())

    def test_search_nonexistent_book(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.store.search_book("Nonexistent")
            self.assertIn("No book found with title 'Nonexistent'", fake_out.getvalue())

    def test_display_books(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.store.display_books()
            output = fake_out.getvalue()
            self.assertIn("Books available in the store:", output)
            self.assertIn("Title: Title A", output)
            self.assertIn("Title: Title B", output)

    def test_display_books_empty_store(self):
        empty_store = BookStore()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            empty_store.display_books()
            self.assertIn("No books in the store.", fake_out.getvalue())

if __name__ == "__main__":
    unittest.main()