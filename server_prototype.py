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
import threading

# Should be used to lock the server from typing when there is another connection used.
# Should be tested without it to see if there will be no issues.
print_lock = threading.Lock()

def handle_connection(conn) -> None:
    while True:
        data = conn.recv(1024)
        if not data:
            print('Connection terminated')
            print_lock.release()
            break

        # Send the data back to the client
        game_name = str(data.decode('ascii'))
        respond = [0, 0]
        if game_name == 'Red dead redemtion 2':
            respond = [29.99, 59.99]
        elif game_name == 'Songs of conquest':
            respond = [15.99, 29.99]
        else:
            print(game_name)

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
        conn, address = s.accept()
        print_lock.acquire()
        print('Connected to address: ', address[0], ':', address[1])
        start_new_thread(handle_connection, (conn,))

    s.close()

if __name__ == '__main__':
    main()
