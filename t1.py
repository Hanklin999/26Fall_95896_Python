import threading
import sys

def count(first: int, last:int)->None:
    for i in range(first, last):
        print(i)

def main():
    print(sys.version)
    first = 1
    last = 10
    t = threading.Thread(target = count, args=(first, last))
    t.start( )
    print('Main finishes')
    
if __name__ == '__main__':
    main()


