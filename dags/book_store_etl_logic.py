#book_store_etl_logic.py
# import relevant python libraries
import pandas as pd
from pymongo import MongoClient
import requests
from dotenv import dotenv_values

#Extract data from book store API
url = 'https://full-stack-bookstore-mern-backend.vercel.app/api/books'
response = requests.get(url)

#parse response to json
data = response.json()

# create a connection string
config = dotenv_values(".env")


# create an engine and load data to a mongodb database
client = MongoClient(config["CONNECTION_STRING"])
mydB = client[config["DB_NAME"]]

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
