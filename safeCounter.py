import threading

count = 0
MAXIMUM = 10000
lock = threading.Lock()

def counter():
    global count
    global lock
    for i in range(MAXIMUM):
        with lock:
            count = count + 1


def main():
    global count
    t1 = threading.Thread(target = counter)
    t2 = threading.Thread(target = counter)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('count = ', count)
    
if __name__ == '__main__':
    main()

