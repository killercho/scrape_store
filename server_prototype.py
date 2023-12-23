'''
    Prototype for a server in a server-client application.
    The server in this version is expected to get input from the client
    convert it to something that the scraper can use and then return an
    array of two numbers that corespond to the original and the discounted prices.
    Example: Red dead redemtion 2 -> red+dead+redemtion+2 -> [29.99, 59.99]
    The server uses multithreading with a thread for every connection.
'''
# Impoting all necessary modules and libraries
import socket, pickle
from _thread import *

# Constants
TRANSFER_SIZE = 1024


def handle_connection(conn) -> None:
    '''
    Function handling the single connection to a single client.
    '''
    while True:
        # Data received from the client
        # 1024 should be big enough but if needed can be increased
        data = conn.recv(TRANSFER_SIZE)
        if not data:
            print('Connection terminated')
            break

        # Decode and process the data from the client
        # Web scraping happens here
        game_name = str(data.decode('ascii'))
        respond = [0, 0]
        if game_name == 'Red dead redemtion 2':
            respond = [29.99, 59.99]
        elif game_name == 'Songs of conquest':
            respond = [15.99, 29.99]
        else:
            print(game_name)

        # Send the data back to the client with pickle to encode it
        conn.send(pickle.dumps(respond))
    conn.close()


def main() -> None:
    HOST = ''
    PORT = 12122

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    print('Server binded to port: ', PORT)

    s.listen()
    print('Server is listening for connections...')

    while True:
        conn = None
        try:
            # Create a connection when a client requests it on a different thread
            conn, address = s.accept()
            print('Connected to address: ', address[0], ':', address[1])
            start_new_thread(handle_connection, (conn,))

        except KeyboardInterrupt:
            # Happens when Ctrl+C is pressed
            if conn:
                conn.close()
            print('\nClosing all connecitons and exiting...')
            break

    s.close()


if __name__ == '__main__':
    main()
