def exercise1():
    t1 = threading.Thread(target=make_pants, args=("green",))
    t2 = threading.Thread(target=make_dress, args=("blue",))

    t1.start()
    t2.start()

    print("middle function!")

    t1.join()
    t2.join()