import datetime
import socket ,time

  # you put your server IP if you windows go to Command prompt and put ipconfig   192.168.100.6

Server_IP = input(" Enter the server IP address")
Port = 50000

def is_number(number):

    try:
        float(number)
        return True

    except:
        return False
def start_client():

 # creating  socket object , AF_INET this used for ipv4 and the other part determine the
 # protocol SOCK_STREAM for TCP and SOCK_DGRAM for UDP

 client_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
 client_socket.connect((Server_IP,Port))
 print("-------------------------------------------------------------------- \n")
 print(f" you are connected to the server that has this IP address {Server_IP} at \n")
 print("-------------------------------------------------------------------- \n")

 while True :
     base =input(" enter Base or type E to quit")

     #Exit
     if base.lower() =="e" :
         break

     # check the number
     if not is_number(base) :
         print(f"✖️ {base} invalid base ")
         continue

     while True:
      exponent = input(" enter Exponent or type E to quit ")

      # Exit
      if exponent.lower() =="e" :
          print("\n------------------------------------------------------------------------")
          print(" ✖️ connection closed  ")
          input("Press enter to Exit")
          client_socket.close()
          return


         # check the number
      if not is_number(exponent):
          print(f"✖️ {exponent} invalid exponent  ")
          continue

      # Processing of data for sending
      packet = f"{base},{exponent}"

     #starting calculate RTT
      start = time.perf_counter()

      client_socket.send(packet.encode())

     # receiving result from server
      result = client_socket.recv(100).decode()

     # stop time
      end = time.perf_counter()

     #RTT in ms
      RTT =(end - start) * 1000

      print(f"\n ✅ result is {result} ")
      print(f"⏱️ RTT is {RTT:.4f}ms")
      break

 print("\n------------------------------------------------------------------------")
 print(" ✖️ connection closed  ")
 input("Press enter to Exit")
 client_socket.close()

if __name__=="__main__":
    start_client()