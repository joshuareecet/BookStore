"""This module fills the config file
"""


import json

def getConfig():
  """Collects inputs required from the user to fill the config file.
  
  Arguments
  -----
    none


  Returns
  ------
    none
  """
  with open("config.json","w") as config_file:
    config_dict = {}
    config_dict["api_key"] = input("Please enter your API key: ")
    config_file.write(json.dumps(config_dict, indent=2))


# Loading from the config file - just api keys for now
try:
  with open("config.json") as config_file:
    config_dict = json.loads(config_file.read())
    api_key = config_dict["api_key"]
    print(api_key)
except FileNotFoundError:
  getConfig()
except KeyError:
  print("Error: config.json does not contain the correct values. Please follow instructions below: ")
  getConfig()
except:
  raise Exception("Something went wrong when reading config.json")
