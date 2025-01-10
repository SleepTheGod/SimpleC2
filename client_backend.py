import socket
from cryptography.fernet import Fernet

# Load the key (assuming you have the server_key.key file from the server)
with open('server_key.key', 'rb') as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)

# TCP client function
def tcp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9999))  # Connect to the server
    
    # Authenticate with the server
    password = input("Enter password: ")
    client.send(password.encode('utf-8'))
    response = client.recv(1024).decode('utf-8')
    print(response)
    if "failed" in response:
        client.close()
        return

    while True:
        command = input("Enter command (get <filename>, put <filename>, exit): ")
        
        # Encrypt the command before sending
        encrypted_command = cipher_suite.encrypt(command.encode('utf-8'))
        client.send(encrypted_command)

        if command == "exit":
            encrypted_response = client.recv(4096)
            response = cipher_suite.decrypt(encrypted_response).decode('utf-8')
            print(f"Received TCP: {response}")
            break
        elif command.startswith("get "):
            filename = command.split()[1]
            with open(f"received_{filename}", 'wb') as f:
                while True:
                    data = client.recv(1024)
                    if not data:
                        break
                    f.write(cipher_suite.decrypt(data))  # Decrypt received data
        elif command.startswith("put "):
            filename = command.split()[1]
            try:
                with open(filename, 'rb') as f:
                    data = f.read(1024)
                    while data:
                        encrypted_data = cipher_suite.encrypt(data)  # Encrypt before sending
                        client.sendall(encrypted_data)
                        data = f.read(1024)
            except FileNotFoundError:
                print("File not found")
        else:
            encrypted_response = client.recv(4096)
            response = cipher_suite.decrypt(encrypted_response).decode('utf-8')
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
