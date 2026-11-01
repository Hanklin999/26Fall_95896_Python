import threading

def count(first: int, last:int)->None:
    for i in range(first, last):
        print('Thread: i = ', i)

def main():
    first = 1
    last = 100
    t = threading.Thread(target = count, args=(first, last))
    t.start( )
    for i in range(first, last):
        print('Main: i = ', i)
    print('Main finishes')

    
if __name__ == '__main__':
    main()


