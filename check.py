import requests
import pandas as pd
from bs4 import BeautifulSoup

# 1. Perform a GET request on the Space X API
response = requests.get("https://api.spacexdata.com/v4/launches")
data = response.json()


# Convert the response to a DataFrame using pd.json_normalize
df = pd.json_normalize(data)

# Perform a GET request on the SpaceX API
#response = requests.get("https://api.spacexdata.com/v4/launches")
#data = response.json()

launches_response = requests.get("https://api.spacexdata.com/v4/launches")
launches_data = launches_response.json()


# Convert the response to a DataFrame
#df = pd.json_normalize(data)
df = pd.json_normalize(launches_data)


# Get the year from the first row in the column static_fire_date_utc
first_row_static_fire_date = pd.to_datetime(df['static_fire_date_utc'].iloc[0])
year_first_row = first_row_static_fire_date.year
print("Question 1 Answer:", year_first_row)

# Fetch rocket details
rockets_response = requests.get("https://api.spacexdata.com/v4/rockets")
rockets_data = rockets_response.json()
rockets_df = pd.json_normalize(rockets_data)

# Create a mapping of rocket IDs to rocket names
#rocket_id_to_name = rockets_df.set_index('id')['name'].to_dict()
rocket_id_to_name = rockets_df.set_index('id')['name'].to_dict()
# Map rocket IDs in the launches DataFrame to rocket names
#df['rocket_name'] = df['rocket'].map(rocket_id_to_name)

df['rocket_name'] = df['rocket'].map(rocket_id_to_name)

falcon_9_count = df[df['rocket_name'] == 'Falcon 9'].shape[0]
print("Question 2 Answer:", falcon_9_count)

# Check for missing values in the 'launchpad' column
if 'launchpad' in df.columns:
    missing_values_launchpad = df['launchpad'].isnull().sum()
    print("Question 3 Answer:", missing_values_launchpad)
else:
    print("Column 'launchpad' does not exist in the DataFrame.")
