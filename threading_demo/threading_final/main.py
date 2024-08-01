import threading

def make_pants(color):
    print(f"Making {color} pants!")

def make_dress(color):
    print(f"Making {color} dress!")

if __name__ =="__main__":
    t1 = threading.Thread(target=make_pants, args=("green",))
    t2 = threading.Thread(target=make_dress, args=("blue",))

    