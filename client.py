import socket
import sys


def main():
    clientSocket = None

    try:
        # Create the client socket and connect to the server
        # There is no guarantee that port 8001 is free
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        #add customized host
        address = "localhost"
        port = 8001
        
        if len(sys.argv) == 3:
            address = sys.argv[1]
            port = int(sys.argv[2])
        
        clientSocket.connect((address, port))

        # Create file objects for sending and receiving text
        inFile = clientSocket.makefile("r")
        outFile = clientSocket.makefile("w")
        

        
        
        #LOOP
        
        
        while True:
            # For now, a hard-coded message to send
            outMessage = input("Enter your message: ")            

            # Send the message to the server
            outFile.write(outMessage + "\n")
            outFile.flush()
            
            # Check whether to quit
            if outMessage.strip() == "QUIT":
                break
    
            # Receive the reply
            inMessage = inFile.readline()
            print(inMessage.strip())
            
            # inMessage 也一起可以跳脫 loop
            
            if inMessage.strip() == "QUIT":
                break

    except Exception as e:
        print(e)

    finally:
        if clientSocket is not None:
            print("Closing client socket...")
            clientSocket.close()


if __name__ == "__main__":
    main()