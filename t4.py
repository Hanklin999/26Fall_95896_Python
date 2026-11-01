import threading

def count(first: int, last:int)->None:
    sum = 0
    for i in range(first, last):
        sum = sum + i
    print('Thread finished, answer = ', sum)

def main():
    first = 1
    last = 1000000
    t = threading.Thread(target = count, args=(first, last))
    t2 = threading.Thread(target = count, args=(-last, -first))
    t.start( )
    t2.start( )
    
if __name__ == '__main__':
    main()


