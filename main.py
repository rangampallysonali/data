# requirements.txt
# pandas
# requests
import pandas as pd
import requests

def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes
    return response.json()

def process_data(data):
    df = pd.DataFrame(data)
    print(df.head())
    print(df.describe())

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos" # Example API endpoint
    try:
        data = fetch_data(url)
        process_data(data)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")