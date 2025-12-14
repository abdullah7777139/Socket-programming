import socket,threading,datetime

HOST ="0.0.0.0" #allow all client to connect
PORT = 50000

def start_server():
    # creating  socket object , AF_INET this used for ipv4 and the other part determine
    # protocol SOCK_STREAM for TCP and SOCK_DGRAM for UDP
    server_socket =socket.socket(socket.AF_INET , socket.SOCK_STREAM)

    # bind the server socket to the specific host and port#
    server_socket.bind((HOST,PORT))

    #put socket in listening mode
    # 7 is the number of the maximum queued connections
    server_socket.listen(7)

    print(" ✅ Server is running and listening for any connections .......... \n")

    # accept client continuously
    while True:
        client_socket,client_address = server_socket.accept()

        #creating new thread to handle each client
        client_thread = threading.Thread(
            target=servicing_client,
            args=(client_socket,client_address)
        )
        client_thread.start()


#
def servicing_client(client_socket,client_address):

    print(f"✅ New connection from {client_address} at {datetime.datetime.now()} \n")

    while True :
        try:
            #receiving base,exponent from client
            data =client_socket.recv(100).decode()

            # client is disconnected exit the loop
            if not data :
                break

            # handle base,exponent
            base,exponent =data.split(",")
            base=float(base)
            exponent=float(exponent)

            print(f"client with this IP {client_address} send {base},{exponent} at {datetime.datetime.now()}\n")

            result = base ** exponent

            # sending result to client
            client_socket.send(str(result).encode())

        # handle any unexpected errors
        except Exception as e:
            print(f" ✖️ error with the client {client_address} {e} \n")
            break

    print(f"✖️ connection is closed with {client_address} at {datetime.datetime.now()}\n")

if __name__=="__main__":
    start_server()