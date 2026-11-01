import socket
import sys


def main():
    serverSocket = None
    clientConnection = None

    try:
        # Create the server socket
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # set port number
        port = 8001
        
        if len(sys.argv) == 2:
            port = int(sys.argv[1])
        
        
        serverSocket.bind(("", port))

        serverSocket.listen(1)

        # Wait for a client to connect
        clientConnection, address = serverSocket.accept()

        # Create file objects for reading and writing text
        inFile = clientConnection.makefile("r")
        outFile = clientConnection.makefile("w")

        #While Loop
        while True:
            
            # Get the input message
            message = inFile.readline()
            print("Server:", message.strip())
            
            if message.strip() == "QUIT":
                break
    
            # Send the reply
            reply = input("Enter your reply: ")
            outFile.write(reply + "\n")
            outFile.flush()
            
            # Client can break
        
            if reply.strip() == "QUIT":
                break

    except Exception as e:
        print(e)

    finally:
        if clientConnection is not None:
            clientConnection.close()

        if serverSocket is not None:
            print("Closing server socket...")
            serverSocket.close()


if __name__ == "__main__":
    main()