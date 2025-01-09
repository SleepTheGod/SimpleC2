import socket
import threading
import os
import pyautogui
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify, send_file
from datetime import datetime

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Save the key to a file (to be shared securely with the client)
with open('server_key.key', 'wb') as key_file:
    key_file.write(key)

app = Flask(__name__)

# Session logs
session_logs = []

# Print banner in red text
def print_banner():
    banner = """
    \033[91m
    ███████╗██╗     ███████╗███████╗██████╗     ████████╗ ██████╗  ██████╗ ██╗     ███████╗    
    ██╔════╝██║     ██╔════╝██╔════╝██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝    
    ███████╗██║     █████╗  █████╗  ██████╔╝       ██║   ██║   ██║██║   ██║██║     ███████╗    
    ╚════██║██║     ██╔══╝  ██╔══╝  ██╔═══╝        ██║   ██║   ██║██║   ██║██║     ╚════██║    
    ███████║███████╗███████╗███████╗██║            ██║   ╚██████╔╝╚██████╔╝███████╗███████║    
    ╚══════╝╚══════╝╚══════╝╚══════╝╚═╝            ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝    
                                                                                           
    ██████╗ ██████╗ ██████╗      ██████╗ ██╗   ██╗███████╗██████╗     ████████╗ ██████╗██████╗ 
    ██╔══██╗██╔══██╗██╔══██╗    ██╔═══██╗██║   ██║██╔════╝██╔══██╗    ╚══██╔══╝██╔════╝██╔══██╗
    █████╔╝██║  ██║██████╔╝    ██║   ██║██║   ██║█████╗  █████╔╝       ██║   ██║     ██████╔╝
    ██╔══██╗██║  ██║██╔═══╝     ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗       ██║   ██║     ██╔═══╝ 
    ██║  ██║██████╔╝██║         ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║       ██║   ╚██████╗██║     
    ╚═╝  ╚═╝╚═════╝ ╚═╝          ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝       ╚═╝    ╚═════╝╚═╝
    \033[0m
    """
    print(banner)

# TCP server function
def tcp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(5)
    print("TCP Server listening on port 9999")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted TCP connection from {addr}")
        client_handler = threading.Thread(target=handle_tcp_client, args=(client_socket, addr))
        client_handler.start()

# Handler for TCP client
def handle_tcp_client(client_socket, addr):
    with client_socket as sock:
        # Log the session
        session_start = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        session_logs.append({"address": addr, "start_time": session_start})

        # Authenticate the client
        sock.send(b"Enter password: ")
        password = sock.recv(1024).decode('utf-8')
        if password != "securepassword":
            sock.send(b"Authentication failed")
            sock.close()
            return
        sock.send(b"Authentication successful")

        while True:
            request = cipher_suite.decrypt(sock.recv(1024)).decode('utf-8')
            if not request:
                break
            print(f"Received TCP: {request}")

            if request == "exit":
                sock.send(cipher_suite.encrypt(b"Connection closed"))
                break
            elif request.startswith("get "):
                filename = request.split()[1]
                if os.path.exists(filename):
                    with open(filename, 'rb') as f:
                        sock.sendall(cipher_suite.encrypt(f.read()))
                else:
                    sock.send(cipher_suite.encrypt(b"File not found"))
            elif request.startswith("put "):
                filename = request.split()[1]
                with open(filename, 'wb') as f:
                    data = cipher_suite.decrypt(sock.recv(1024))
                    while data:
                        f.write(data)
                        data = cipher_suite.decrypt(sock.recv(1024))
            elif request.startswith("screenshot"):
                screenshot = pyautogui.screenshot()
                screenshot.save("screenshot.png")
                with open("screenshot.png", 'rb') as f:
                    sock.sendall(cipher_suite.encrypt(f.read()))
            else:
                sock.send(cipher_suite.encrypt(b"Unknown command"))
        sock.close()

        # Log the session end
        session_end = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        session_logs[-1]["end_time"] = session_end

# Flask endpoints
@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "Server is running"})

@app.route('/screenshot', methods=['GET'])
def screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    return send_file("screenshot.png", mimetype='image/png')

@app.route('/files', methods=['GET'])
def list_files():
    files = os.listdir('.')
    return jsonify(files)

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    if os.path.exists(filename):
        return send_file(filename, as_attachment=True)
    else:
        return jsonify({"error": "File not found"}), 404

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save(file.filename)
    return jsonify({"status": "File uploaded successfully"})

@app.route('/logs', methods=['GET'])
def get_logs():
    return jsonify(session_logs)

# Start the TCP server in a separate thread
tcp_thread = threading.Thread(target=tcp_server)
tcp_thread.start()

if __name__ == '__main__':
    print_banner()
    app.run(host='0.0.0.0', port=5000)
