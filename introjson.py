# Big data sets are often storered or extrated as JSON
# JSON is plain text, but has the format of an object.
# Json objects have the same format as Python dictionaries.

# Load Json file into a DataFrame:
import pandas as pd
df = pd.read_json('dataprueba.json')
print(df.to_string()) #using 'to_string()' to print the entire DataFrame 

# If the Json code is not in a file, but in a Python dictionary,
# we can load it into a DataFrame directly.
# Load a Python dictionary into a DataFrame:

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409.1,
    "1":479.0,
    "2":340.0,
    "3":282.4,
    "4":406.0,
    "5":300.5
  }
}

df = pd.DataFrame(data)
print(df)