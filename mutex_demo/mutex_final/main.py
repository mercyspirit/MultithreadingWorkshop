import time
import threading
import concurrent.futures
from request_service import get
from json_service import write_to_file
import re

survey_dictionary_count = {}
global counter
counter = 0
lock = threading.Lock()

def add_row_to_dictionary(winning_numbers):
    global counter
    
    # Perform non-critical operations outside of the lock
    time.sleep(0.03)
    numbers_list = winning_numbers.split()
    
    for item in numbers_list:
        time.sleep(0.004)
        
        # Lock only the critical section where shared data is modified
        with lock:
            if item not in survey_dictionary_count:
                survey_dictionary_count[item] = 1
            else:
                survey_dictionary_count[item] += 1
            counter += int(item)

if __name__ == '__main__':
    print("Program start")
    start = time.time()

    body = get('https://data.ny.gov/api/views/d6yy-54nr/rows.json?accessType=DOWNLOAD')
    data = body["data"]
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        futures = []
        for row in data:
            futures.append(executor.submit(add_row_to_dictionary, row[9]))
                
        for future in concurrent.futures.as_completed(futures):
            future.result()

    print(survey_dictionary_count)
    print(counter)
    end = time.time()
    difference = end - start
    print(f"Time elapsed: {difference}")