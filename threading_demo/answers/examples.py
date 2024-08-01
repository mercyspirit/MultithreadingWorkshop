def exercise1():
    t1 = threading.Thread(target=make_pants, args=("green",10))
    t2 = threading.Thread(target=make_dress, args=("blue",10))

    t1.start()
    t2.start()

    t1.join()
    t2.join()