import socket  
  
# Define the IP address and port for the server honeypot to listen on  
HOST = '0.0.0.0'  # Listen on all available network interfaces  
PORT = 8080  
  
# Function to handle incoming connections  
def handle_connection(client_socket, client_address):  
    # Log the connection details  
    print(f"== NEW CONNECTION FROM {client_address} AT {datetime.datetime.now()} ==")  
  
    # Send a fake response to the client  
    response = b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"  
    response += b"<html><head><title>Internal Server</title></head>"  
    response += b"<body><h1>Internal Server</h1>"  
    response += b"<p>Welcome Admin</p></body></html>"  
    client_socket.sendall(response)  
  
    # Close the client connection  
    client_socket.close()  
  
# Main function to create and listen for incoming connections  
def main():  
    # Create a TCP socket  
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
  
    # Allow reusing the same address  
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  
  
    # Bind the socket to the IP address and port  
    server_socket.bind((HOST, PORT))  
  
    # Start listening for incoming connections  
    server_socket.listen(5)  
    print(f"server honeypot listening on port {PORT}...")  
  
    while True:  
        # Accept incoming connection  
        client_socket, client_address = server_socket.accept()  
        handle_connection(client_socket, client_address)  
  
if __name__ == "__main__":  
    import datetime  
    main()
