'''
    Prototype for a client in a server-client application.
    The client in this version is expected to sent input from the user
    and print the answer that the server returned from the connection.
    The server answer is in the form of a price that the web scraper scraped.
    Example: Red dead redemption 2 -> [29.99, 59.99]
    where the first value is the reduced price of the game
    and the second one is the original value of the game.
    If the prices are the same then appropriate output should be displayed.
    With the prices there should be info for the amount saved by the user
    and the procentale of the sale atm.
'''

import socket, pickle

# Constatns
TRANSFER_SIZE = 1024

def main() -> None:
    # Server ip
    HOST = '127.0.0.1'
    PORT = 12122

    # Creating the connection
    # TODO: Handle rejection from the server in the actual app (with a trycatch?)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    # Create a message for the server
    message = input('Enter a game name: ')
    while True:
        # Send a message to the server encoded
        s.send(message.encode('ascii'))
        # Receive the serve's response
        data = s.recv(TRANSFER_SIZE)

        # Output the information from the server
        print('Received from the server: ', str(pickle.loads(data)))

        # Enter a new message for the server or exit
        message = input('Enter another game or "no" to exit: ')
        if message == 'no':
            break
    s.close()

if __name__ == '__main__':
    main()
