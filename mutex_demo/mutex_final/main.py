import time
from request_service import get
from json_service import write_to_file
import re

if __name__ == '__main__':
    print("Program start")
    start = time.time()

    survey_dictionary_count = {}

    body = get('https://data.cdc.gov/api/views/hn4x-zwk7/rows.json?accessType=DOWNLOAD')
    data = body["data"]
    # 10 location


    for row in data:
        winning_numbers = row[9]
        numbers_list = winning_numbers.split()
        for item in numbers_list:
            if item not in survey_dictionary_count:
                survey_dictionary_count[item] = 1
            else:
                survey_dictionary_count[item] = survey_dictionary_count[item] + 1
    print(survey_dictionary_count)
    end = time.time()
    difference = end - start
    print(f"Time elapsed: {difference}")