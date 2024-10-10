import time
import threading
import concurrent.futures
import re
from lottery-data import getData

survey_dictionary_count = {}
counter = 0
even_odd_sum = 0
lock = threading.Lock()

def add_row_to_dictionary(winning_numbers):
    global counter
    global even_odd_sum
    # Perform non-critical operations outside of the lock
    time.sleep(0.06)
    numbers_list = winning_numbers.split()
    
    for item in numbers_list:
        time.sleep(0.008)
        
        # Lock only the critical section where shared data is modified
        with lock:
            if item not in survey_dictionary_count:
                survey_dictionary_count[item] = 1
            else:
                survey_dictionary_count[item] += 1
            counter += int(item)
            
            if int(item) % 2 > 0:
                even_odd_sum += int(item)
            else:
                even_odd_sum -= int(item)

if __name__ == '__main__':
    print("Program start")
    start = time.time()

    # data sourced from 'https://data.ny.gov/api/views/d6yy-54nr/rows.json?accessType=DOWNLOAD', downloaded on 9/22/2024
    data = getData()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
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
    print(even_odd_sum)
