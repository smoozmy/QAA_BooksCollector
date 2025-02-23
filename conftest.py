import pytest
from books_collector import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()