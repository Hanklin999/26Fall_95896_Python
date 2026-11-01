import threading

data = [i for i in range(1000)]
i = 0

def show()->None:
    global i
    print('Thread starting')
    while i < 1000:
        print('Thread: data[i] = ', data[i])
        i = i + 1

def main():
    t = threading.Thread(target = show)
    global i
    while i < 1000:
        print('Main: data[i] = ', data[i])
        i = i + 1
    t.start( )
    print('Main finishes')

    
if __name__ == '__main__':
    main()


