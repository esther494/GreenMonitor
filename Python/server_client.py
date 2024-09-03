import socket

class ServerClient:
    # ESP32 Configurations:
    SERVER_IP = '192.168.2.42'
    SERVER_PORT = 81

    def __init__(self):
        # This data will be used initially and in case of an invalid data
        self.last_received_data = "0.0,0.0,0.0,0.0"

        # Error code
        self.error_code = 0

        # Create a TCP socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # Bind the socket to the IP and port
            self.server_socket.bind((self.SERVER_IP, self.SERVER_PORT))

            # Start listening for incoming connections
            self.server_socket.listen(1)  # 1 means the server can handle one connection at a time
            print(f"Listening on {self.SERVER_IP}:{self.SERVER_PORT}...")

            # Accept an incoming connection
            self.client_socket, self.client_address = self.server_socket.accept()
            print(f"Connection from {self.client_address} has been established.")
        except socket.error as e:
            print(f"Error Code 3: Socket error: {e}")
            self.error_code = 3
            self.server_socket.close()
        except Exception as e:
            print(f"Error Code 4: An unexpected error occurred: {e}")
            self.error_code = 4
            self.server_socket.close()

    def process_data(self, data):
        try:
            decoded_data = data.decode('utf-8').strip()
            if decoded_data.count(',') == 3:  # Valid data with 3 commas
                self.last_received_data = decoded_data
        except Exception as e:
            print(f"Error Code 5: Error processing data: {e}")
            self.error_code = 5

    def get_last_received_data(self):
        return self.last_received_data

    def close(self):
        """Close the client and server sockets."""
        if hasattr(self, 'client_socket'):
            self.client_socket.close()
        if hasattr(self, 'server_socket'):
            self.server_socket.close()
