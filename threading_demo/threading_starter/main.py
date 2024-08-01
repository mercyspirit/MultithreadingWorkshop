import threading
import time

def make_pants(color, number):
    for i in range(number):
        print(f"{i}: Making {color} pants!")
        time.sleep(1)


def make_dress(color, number):
    for i in range(number):
        print(f"{i}: Making {color} dress!")
        time.sleep(1)
    

if __name__ =="__main__":
    start_time = time.time()
    print("Boss: I need to make some clothes")
    make_pants("green", 10)
    make_dress("blue", 10)

    print("Clothes done! I'm leaving!")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")