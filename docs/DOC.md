# Script to Collect Data from Json API PlaceHolder and Process Them

This script aims to collect data from a JSON PlaceHolder API, process the data, and print the names that contain 5 or more vowels.

## Functionality

The script performs the following steps:

1. Makes a GET request to the JSON PlaceHolder API URL to retrieve the data.
2. Checks if the response status code is 200 (OK). Otherwise, an exception is raised.
3. Converts the JSON response into a Pandas DataFrame for easy data visualization and processing.
4. Iterates over the names in the DataFrame and counts the number of vowels in each name.
5. Prints the names that have 5 or more vowels.

## How to Use

1. Make sure you have the `requests` and `pandas` libraries installed.
2. Set the URL_ENDPOINT to the desired JSON PlaceHolder API endpoint.
3. Run the script.

## Main Functions

- `get_endpoint_valuable_data()`: Performs a GET request to the JSON PlaceHolder API and returns the JSON response, status code, and response as text.
- `check_status_code_isOK(status_code)`: Checks if the status code is equal to the expected status code (200). Otherwise, it raises an exception.
- `convert_json_to_dataframe(json_response)`: Converts the JSON response into a Pandas DataFrame, setting the index as 'id'.
- `print_names_that_contains_5_or_more_vowels(dataframe)`: Iterates over the names in the DataFrame and prints the names that contain 5 or more vowels.

## Example Usage

```python
import requests
import pandas as pd

# Define URL_ENDPOINT and other constants

# Functions and main code block

if __name__ == '__main__':
    raw_response, status_code = get_endpoint_valuable_data()
    check_status_code_isOK(status_code)
    data_frame_with_user_infos = convert_json_to_dataframe(raw_response)
    print_names_that_contains_5_or_more_vowels(data_frame_with_user_infos)
```