import threading

lock = threading.Lock()

def example_one(winning_numbers):
    global counter
    
    # Perform non-critical operations outside of the lock
    time.sleep(0.03)
    numbers_list = winning_numbers.split()
    
    for item in numbers_list:
        time.sleep(0.004)
        
        # Lock only the critical section where shared data is modified
        lock.acquire()
            if item not in survey_dictionary_count:
                survey_dictionary_count[item] = 1
            else:
                survey_dictionary_count[item] += 1
            counter += int(item)
        lock.release()

def example_two(winning_numbers):
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