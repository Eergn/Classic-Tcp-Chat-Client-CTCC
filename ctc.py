import socket
import threading


Server = input("Server Address >> ")
Username = input("Choose a Username >> ")


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((Server,65432))


def recive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if (message=="Username? >> "):
                client.send(Username.encode("ascii"))
            else:
                print(message)
        except:
            print("An Error occurred! ")
            client.close()
            break

def write():
    while True:
        message = f'{Username} >> {input(f"{Username} >> ")} \n'
        client.send(message.encode("ascii"))

recive_thread = threading.Thread(target=recive)
recive_thread.start()


write_thread = threading.Thread(target=write())
write_thread.start()
