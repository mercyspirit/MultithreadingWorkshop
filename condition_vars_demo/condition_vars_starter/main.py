import threading

condition = threading.Condition()

queue_mutex = threading.Lock()

request_queue = []

def process_request_queue():
    with queue_mutex:
        # do process requests
        while not request_queue:
            print("waiting")
        request = request_queue.pop(0)
        print(request)
