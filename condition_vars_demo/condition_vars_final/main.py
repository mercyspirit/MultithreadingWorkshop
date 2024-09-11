import threading
import random
import time

condition = threading.Condition()
request_queue = []

# Event to signal stopping the threads
stop_event = threading.Event()

# Generator function to create an infinite stream of random numbers
def random_number_stream():
    while not stop_event.is_set():
        sleep_duration = random.uniform(0, 1)
        time.sleep(sleep_duration)
        random_string = random.choice(["pants", "dress", "shirt"])
        yield { "clothing": random_string, "number": random.randint(1, 5) }  # Yields a random float between 0 and 1

# Producer function that generates random numbers and puts them in the queue
def producer():
    for random_number in random_number_stream():
        with condition:
            request_queue.append(random_number)
            clothing = {random_number["clothing"]}
            number = {random_number["number"]}
            print(f"Ordered: {number} {clothing}")
            condition.notify()  # Notify all consumers that a new item is available

# Consumer function that waits for random numbers and processes them
def consumer(consumer_id):
    while not stop_event.is_set():
        with condition:
            while not request_queue and not stop_event.is_set():  # Wait until something is available in the queue
                print(f"Consumer {consumer_id} is waiting for a number...")
                condition.wait()  # Wait until the producer notifies
            if request_queue:
                request = request_queue.pop(0)
        clothing = request["clothing"]
        for num in range(request["number"]):
            time.sleep(1)
            print(f"Consumer {consumer_id} created: {clothing}")
            time.sleep(1)  # Simulating processing time

if __name__ == '__main__':
    # Start the producer thread
    producer_thread = threading.Thread(target=producer)
    producer_thread.start()

    # Start three consumer threads
    consumer_threads = []
    for i in range(3):
        thread = threading.Thread(target=consumer, args=(i,))
        consumer_threads.append(thread)
        thread.start()

    try:
        # Let the program run for some time (e.g., 500 seconds)
        time.sleep(500)
    except KeyboardInterrupt:
        print("\nReceived KeyboardInterrupt. Exiting gracefully...")

    # Set the stop_event to stop the threads
    stop_event.set()

    # Notify all consumers in case they are waiting
    with condition:
        condition.notify_all()

    # Wait for all threads to finish
    producer_thread.join()
    for thread in consumer_threads:
        thread.join()

    print("Program exited.")