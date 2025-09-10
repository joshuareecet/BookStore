from pathlib import Path
import config
from web import search , web_book_converter
from user_library.storage import Book , BookLibrary

def main():
 search_results = search.conductSearch()
 tempLibrary = BookLibrary()
 web_book_converter.convertToLibrary(search_results, tempLibrary)
 i = 1
 print("Books found include: \n")
 for books in tempLibrary.books():
  print(f"{i}: {books.title()}")
  i += 1

main()
