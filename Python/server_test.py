import unittest
from unittest.mock import MagicMock, patch
import socket

# Replace 'server_client' with the actual name of your module
from server_client import ServerClient  

class TestServerClient(unittest.TestCase):

    @patch('main.socket.socket')
    def setUp(self, mock_socket):
        # Mock the socket and its methods
        self.mock_server_socket = MagicMock()
        self.mock_client_socket = MagicMock()
        
        # Configure the mock socket to return the mocked server and client sockets
        mock_socket.return_value = self.mock_server_socket
        self.mock_server_socket.accept.return_value = (self.mock_client_socket, ('127.0.0.1', 12345))

        # Create an instance of ServerClient
        self.client = ServerClient()

    def test_initialization(self):
        # Check if the server socket was created, bound, and set to listen
        self.assertTrue(self.mock_server_socket.bind.called)
        self.assertTrue(self.mock_server_socket.listen.called)
        self.assertTrue(self.mock_server_socket.accept.called)

    def test_process_data(self):
        # Mock data to process
        test_data = "10.5,20.3,30.2,40.1".encode('utf-8')
        self.client.process_data(test_data)
        
        # Verify that the last received data was updated
        self.assertEqual(self.client.get_last_received_data(), "10.5,20.3,30.2,40.1")

    def test_process_invalid_data(self):
        # Mock invalid data
        test_data = "invalid_data".encode('utf-8')
        self.client.process_data(test_data)
        
        # Verify that the last received data remains unchanged
        self.assertEqual(self.client.get_last_received_data(), "0.0,0.0,0.0,0.0")

    def test_close(self):
        # Call the close method
        self.client.close()
        
        # Verify that the client and server sockets are closed
        self.mock_client_socket.close.assert_called_once()
        self.mock_server_socket.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
