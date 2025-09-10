
class Book():
  def __init__(self, authors=None, title=None, publisher=None, description=None, kind=None, language=None, categories=None, thumbnail = None):
    self._authors = authors
    self._title = title
    self._publisher = publisher
    self._description = description #description of the book
    self._kind = kind #kind: book / magazine
    self._language = language
    self._categories = categories
    self._thumbnail = thumbnail

  def authors(self):
    return self._authors
  
  def title(self):
    return self._title
  
  def publisher(self):
    return self._publisher
  
  def description(self):
    return self._description

  def kind(self):
    return self._kind

  def language(self):
    return self._language
  

class BookLibrary():
  def __init__(self):
    self._books = []
    self._size = 0
  
  def books(self):
    return self._books

  def size(self):
    return self._size
  
  def addBook(self, book: Book):
    self._books.append(book)
    self._size += 1

  def removeBook(self, removal_method, target):
    removal_method = getAttribute()
    for book in self._books:
      if getattr(book, removal_method) == target:
        self._books.remove(book)
        self._size -= 1
    raise ValueError("Book does not exist in the user's library")

  def findBook(self, book):
    target = book
    for items in self._books:
      if items == target:
          return items
    raise ValueError("Book does not exist in the user's library")

def getAttribute():
  attribute_dict = {
    1: 'author',
    2: 'title',
    3: 'publisher',
    4: 'description',
    5: 'kind',
    6: 'language'
  }
  
  i = 0
  while True:
    if i > 10:
      print("ERROR: too many errors, program exited\n")
      return -1
    user_selection = input("\nPlease pick the attribute to search by:\n" 
    "1. author\n"
    "2. title\n"
    "3. publisher\n"
    "4. description\n"
    "5. kind\n"
    "6. language\n"
    "0. Cancel search.\n")
    
    try:
      user_selection = int(user_selection.strip())
      if user_selection in attribute_dict:
        attribute = attribute_dict[user_selection]
        return attribute
      else:
        print("Please enter a valid number in the range 0 < number < 7")
    
    except:
      print("ValueError: Please enter a valid number!")
      i += 1

def main():
  user_library = BookLibrary()

if __name__ == "__main__": 
  main()

