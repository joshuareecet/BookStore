from user_library.storage import Book, BookLibrary

def convertToLibrary(search_result, library: BookLibrary):
  for items in search_result['items']:
    library.addBook(Book(
        title=items['volumeInfo']['title'],
        authors=items['volumeInfo'].get('authors', []),
        publisher=items['volumeInfo'].get('publisher', ''),
        description=items['volumeInfo'].get('description', ''),
        categories=items['volumeInfo'].get('categories', []),
        thumbnail=items['volumeInfo'].get('imageLinks', {}).get('thumbnail', '')
    ))

  return library

