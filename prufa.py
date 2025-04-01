

import pandas as pd

df = pd.read_csv("movies.csv")
print(df.head())
print(df.info())  # Check for missing values & data types

df.fillna({"release_date": "Unknown", "overview": "No description available"}, inplace=True)

df.drop_duplicates(subset="title", keep="first", inplace=True)

import pandas as pd

movies = pd.read_csv("movies.csv")

# Print some sample movie titles to check formatting
print(movies["title"].head(10))  

# Check if 'Gone Girl' exists in any format
print("Gone Girl" in movies["title"].values)
