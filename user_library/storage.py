
class Book():
  def __init__(self, author=None, title=None, publisher=None, description=None, kind=None, language=None):
    self._author = author
    self._title = title
    self._publisher = publisher
    self._description = description #description of the book
    self._kind = kind #kind: book / magazine
    self._language = language

  def author(self):
    return self._author
  
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
  
  def addBook(self, book: Book):
    self._books.append(book)

  def removeBook(self, removal_method, target):
    removal_method = getAttribute()
    for book in self._books:
      if getattr(book, removal_method) == target:
        return book
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

