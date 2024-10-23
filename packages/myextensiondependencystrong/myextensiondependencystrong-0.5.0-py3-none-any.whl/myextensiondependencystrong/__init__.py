import requests, logging

def hello_world():
    return "Hello from strongbow_v2"

def get_data_from_api(url):
    """Function to make a GET request to an API endpoint and return the response"""
    try:
        # Log the API request
        logging.info(f"Making GET request to {url}")
        
        response = requests.get(url)
        
        # Raise an exception if the request was not successful
        response.raise_for_status()
        
        # Log and return the JSON response
        logging.info("Request was successful. Processing data.")
        return response.json()
    except requests.exceptions.RequestException as e:
        # Log the error and raise it
        logging.error(f"An error occurred: {e}")
        raise
