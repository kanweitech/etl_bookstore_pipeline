#book_store_etl_logic.py
# import relevant python libraries
import pandas as pd
from pymongo import MongoClient
import requests

#Extract data from book store API
url = 'https://full-stack-bookstore-mern-backend.vercel.app/api/books'
response = requests.get(url)

#parse response to json
data = response.json()

# create a connection string
con_str = 'mongodb+srv://odisvybz:I82hkAVaot6y9eKW@cluster0.qxtmbf0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

# create an engine and load data to a mongodb database
client = MongoClient(con_str)
mydB = client['test_data']
collection = mydB['etl']


# create a function and put etl operations
def main():
  # Flatten the data using pandas json_normalize method
  df = pd.json_normalize(data)
  
  df = df[["_id", "title", "description", "category", "trending", "coverImage", "oldPrice", "newPrice", "createdAt", "updatedAt"]]

  # Since just one row was updated, we can't leave other fields as NAN
  df['updatedAt'] = df['createdAt']

  # parse dataframe into a list of dictionaries, because mongodb is an unstructured dbms(stores data as documents i.e key:value pairs)
  dictObject = df.to_dict(orient='records')

  # insert records into destination database
  collection.insert_many(dictObject)

  print("ETL script executed successfully")
