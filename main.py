#import python libraries

import pandas as pd
import requests

# Extract data from API
url = 'https://full-stack-bookstore-mern-backend.vercel.app/api/books'

def main(url):
  response = requests.get(url)
  #print(response)
  # parse response to json
  
  data = response.json()
  #print(data)
  
  # Flatten the data to a dataframe using pandas json_normalize() method
  df = pd.json_normalize(data)
  #print(df)
  
  #lets view the first 5 rows from the top
  #print(df.head())

  # view last 5 rows from the bottom
  #print(df.tail())

  # check the shape of the data frame
  #print(df.shape)

  #check the columns in the dataframe
  #print(df.columns)

  #remove unnecessary column(e.g '__v')
  # create a list an assign the column to it
  column_to_remove = ['__v']
  df = df.drop(columns=column_to_remove)

  #check for duplicates
  print(df.duplicated())

  #check for missing values
  print(df.isnull().sum())

  #check the updatedAt column
  print(df['updatedAt'])

  # we can't leave the updated date that way so we have to populate it
  df['updatedAt'] = df['createdAt']
  print(df['updatedAt'])

  #check the timestamps for data accuracy
  print(df[['createdAt', 'updatedAt']].head())

  #format the timestamps
  df['createdAt'] = pd.to_datetime(df['createdAt'])
  df['updatedAt'] = pd.to_datetime(df['updatedAt'])

  print(df.sample(5))
