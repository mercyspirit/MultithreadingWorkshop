import threading
import concurrent.futures

def exercise1():
    t1 = threading.Thread(target=make_pants, args=("green",10))
    t2 = threading.Thread(target=make_dress, args=("blue",10))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

def exercise2():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for item in clothes:
            if item["type"] == "pants":
                futures.append(executor.submit(make_pants, item["color"], item["number"]))
            elif item["type"] == "dress":
                futures.append(executor.submit(make_dress, item["color"], item["number"]))
                
        for future in concurrent.futures.as_completed(futures):
            print(future.result())