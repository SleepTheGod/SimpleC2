import socket

# TCP client function
def tcp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9999))
    
    while True:
        command = input("Enter command (get <filename>, put <filename>, exit): ")
        client.send(command.encode('utf-8'))
        
        if command == "exit":
            response = client.recv(4096).decode('utf-8')
            print(f"Received TCP: {response}")
            break
        elif command.startswith("get "):
            filename = command.split()[1]
            with open(f"received_{filename}", 'wb') as f:
                data = client.recv(1024)
                while data:
                    f.write(data)
                    data = client.recv(1024)
        elif command.startswith("put "):
            filename = command.split()[1]
            try:
                with open(filename, 'rb') as f:
                    client.sendall(f.read())
            except FileNotFoundError:
                print("File not found")
        else:
            response = client.recv(4096).decode('utf-8')
            print(f"Received TCP: {response}")

    client.close()

# UDP client function
def udp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.sendto(b"Hello UDP Server", ('127.0.0.1', 9998))
    response, _ = client.recvfrom(4096)
    print(f"Received UDP: {response.decode('utf-8')}")

# Run the TCP and UDP clients
tcp_client()
udp_client()
