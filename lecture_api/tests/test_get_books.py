import json
from pprint import pprint

from lecture_api.pages.pages_book_store import PageBookStore

class TestGetBooks:

    def test_get_books(self):
        page = PageBookStore()
        status = page.get_books().status_code
        authors = None
        if status == 200:
            content = json.loads(page.get_books().content)
            authors = set([book.get('autor') for book in content.get('books')])
            for author in set([book.get('autor') for book in content.get('books')]):
                print(author)
            assert len(authors) == 8

