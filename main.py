'''
author: thiagodesouza07t@gmail.com


Script to collect data from Json API PlaceHolder, process them and export as Excel

'''

import requests
import pandas as  pd


#Const Vars
URL_ENDPOINT = "https://jsonplaceholder.typicode.com/users"
OK_STATUS_CODE = 200


def get_endpoint_valuable_data():
    '''Returns the json text response, status code and the raw response'''
    response = requests.get(URL_ENDPOINT)
    return response.text, response.status_code


def check_status_code_isOK(status_code:int):
    '''
    Check if the return CODE is the one setted in the OK_STATUS_CODE in the constant var,
    otherwise raise an RequestException
    '''
    if status_code != OK_STATUS_CODE:        
        raise requests.exceptions.RequestException(f"Error in the response code, wanted {OK_STATUS_CODE}, received {status_code}")
        

def convert_json_to_dataframe(json_response:str):
    '''Convert and minimal process the Json data to the Pandas DataFrame Visualization and Storage'''
    data_frame = pd.read_json(json_response)
    data_frame.set_index('id', inplace=True)
    return data_frame

def print_names_that_contains_5_or_more_vowels(dataframe:pd.DataFrame):
    '''Print the names which contains 5 or more vowels'''
    is_vowel = lambda character: character.lower() in ['a', 'e', 'i', 'o', 'u']
    for name in dataframe['name']:
        count_vowel = 0
        for char in name:
            if is_vowel(char):
                count_vowel += 1
        name_and_vowels_count = {"name" : name, "vowel_count" : count_vowel}
        if name_and_vowels_count.get("vowel_count") > 5:
            print(f"The name {name_and_vowels_count.get('name')} has more than 5 vowels, total : {name_and_vowels_count.get('vowel_count')}")



if __name__ == '__main__':
    raw_response, status_code = get_endpoint_valuable_data()
    check_status_code_isOK(status_code)
    data_frame_with_user_infos = convert_json_to_dataframe(raw_response)
    print_names_that_contains_5_or_more_vowels(data_frame_with_user_infos)

