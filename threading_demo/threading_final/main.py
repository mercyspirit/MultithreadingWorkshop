import concurrent.futures
import time

def make_pants(color, number):
    for i in range(number):
        print(f"{i}: Making {color} pants!")
        time.sleep(1)
    return f"{number} {color} pants done"


def make_dress(color, number):
    for i in range(number):
        print(f"{i}: Making {color} dress!")
        time.sleep(1)
    return f"{number} {color} dresses done"
    

if __name__ =="__main__":
    start_time = time.time()
    print("Boss: I need to make some clothes")
    clothes = [{"color": "green", "type": "pants", "number": 10}, {"color": "blue", "type": "dress", "number": 10}, {"color": "red", "type": "dress", "number": 5}]
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for item in clothes:
            if item["type"] == "pants":
                futures.append(executor.submit(make_pants, item["color"], item["number"]))
            elif item["type"] == "dress":
                futures.append(executor.submit(make_dress, item["color"], item["number"]))
                
        for future in concurrent.futures.as_completed(futures):
            print(future.result())


    print("Clothes done! I'm leaving!")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")