"""A collection of functions for http requests to the google books API
"""

# FOR LATER JOSH!!! INCLUDE PAGINATION TERM in search!!!!!
import requests
import json
from pathlib import Path


#Defining constants
ROOT_DIR = Path(__file__).parent.parent
print(ROOT_DIR)
baseURL = "https://www.googleapis.com/books/v1/volumes?q="


def getSearchType():
  """gets the required search terms
  
  Returns
  ------
    terms (string): A string containing the search type. Returns None if the user cancels, -1 if exits with an error.
  """

  search_type_dict = {
    1: "intitle",
    2: "inauthor",
    3: "inpublisher",
    4: "subject",
    5: "isbn",
    6: "lccn",
    7: "oclc",
    0: None
  }
  
  prompt = ("\nPlease enter the corresponding number for your type of search:\n"
  "1: Book Title\n"
  "2: Author\n"
  "3: Publisher\n"
  "4: Subject / Book Category\n"
  "5: ISBN number\n"
  "6: LCCN (Library of Congress Control Number)\n"
  "7: OCLC (Online Computer Library Center Number)\n"
  "0: Cancel search\n"
  )
  
  i = 0
  while True:
    try:
      user_input = input(prompt) #Could change this later to have terms allow multiple comma seperated values and you can search for each
      user_input = int(user_input.strip())
      
      if user_input in search_type_dict: #would have to change this to a for loop? and we append each item that is in search types. or maybe we make terms iterable
        search_type = search_type_dict[user_input]
        return search_type
      elif i > 10:
        print("Too many errors, program exited.\n")
        return -1
      else:
        print("Value Error: Please enter a valid number 0 < number < 9\n")
        i += 1
    except:
      print("Value Error: Please enter a valid number\n")
      i += 1

def getIsAdvanced():
  """gets the required search type
  
  Returns
  ------
    is_advanced (bool): True = Advanced search, False = Standard search, None = Cancel Search
  """
  
  i = 0
  while True:
    #Exits loop if too many errors have accumulated
    if i > 10:
      print("ERROR: too many errors, program exited\n")
      return -1
  
    
    is_advanced_dict = {
      1: False, #Standard Search
      2: True, #Advanced search
      0: None #Cancel Search
    }
    
    user_selection = input("\nPlease specify the type of search to perform: \n"
    "1: Standard search\n"
    "2: Advanced search (with extra filters)\n"
    "0: Cancel search\n")
    
    try:
      user_selection = int(user_selection.strip())
      if user_selection in is_advanced_dict:
        is_advanced = is_advanced_dict[user_selection]
        return is_advanced
      else:
        print("Please enter a  number within the valid range 0 < num < 4\n")
        i += 1
    except:
      print("ValueError: Please enter a valid number.\n")
      i += 1

def getPrintFilter():
  print_filter_dict = {
      1: "all",
      2: "books",
      3: "magazines",
      0: None
    }

  prompt = "\nPlease pick the print type filter to apply:\n" 
  "1. all - Does not restrict by print type (default).\n"
  "2. books - Returns only results that are books.\n"
  "3. magazines - Returns results that are magazines.\n"
  "0. Cancel search.\n"
  
  i = 0
  while True:
    #Returns if too many errors have accumulated
    if i > 10:
      print("ERROR: too many errors, program exited\n")
      return -1
    user_selection = input(prompt)

    try:
      user_selection = int(user_selection.strip())
      if user_selection in print_filter_dict:
        print_filter = print_filter_dict[user_selection]
        return print_filter
      else:
        print("Please enter a valid number in the range 0 < number < 4")
    
    except:
      print("ValueError: Please enter a valid number!")
      i += 1

def conductSearch():
  
  #Collecting the search type (search by title, author, publisher etc)
  search_type = getSearchType()
  if search_type == None:
    return None
  
  #Collecting the type of medium (book, magazine, both)
  is_advanced = getIsAdvanced()
  if is_advanced == None:
    return None
  if is_advanced == True:
    print_filter = getPrintFilter()
  else:
    print_filter = None

  search_target = input("Please enter your search: ")
  search_target.replace("","+")
  link = baseURL + search_type+":"+search_target
  
  if print_filter is not None:
    link = link + "&printType=" + print_filter
  
  search_result = requests.get(link)
  search_result.raise_for_status()
  
  search_result = search_result.json()
  
  path = Path(ROOT_DIR / 'web' / "dump.json")
  path.write_text(json.dumps(search_result, indent = 4))
#  with open("dump.json","w") as myDump:
#   myDump.write(json.dumps(search_result, indent = 4))

if __name__ == "__main__":
  conductSearch()