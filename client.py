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
    PORT = 12123

    # Creating the connection
    # TODO: Handle rejection from the server in the actual app (with a trycatch?)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((HOST, PORT))

        # Create a message for the server
        message: str = input('Enter a game name: ')
        while True:
            # Send a message to the server encoded
            s.send(message.encode('ascii'))
            # Receive the serve's response
            data: bytes = s.recv(TRANSFER_SIZE)
            data_arr = pickle.loads(data)
            if data_arr[0] == 'No game found':
                print('No game was found. Please check the spelling or search for a new title.\n')
            elif data_arr[1][0] == "0":
                print('Title of the game found: ' + data_arr[0] + '.')
                print('The game found is completely FREE!\n')
            elif data_arr[1][0] == data_arr[1][1]:
                print('Title of the game found: ' + data_arr[0] + '.')
                print('Unfortunatelly the game is not on sale and it\'s price is ' + data_arr[1][0] + '.\n')
            else:
                print('Title of the game found: ' + data_arr[0] + '.')
                print('The game found is on sale from ' + data_arr[1][0] + ' to ' + data_arr[1][1] + '.')
                # Calculate the procentage of the sale
                original_price: float = float(data_arr[1][0][:-1].replace(',', '.'))
                discounted_price: float = float(data_arr[1][1][:-1].replace(',', '.'))
                sale_procentage: float = int(100 * round(1 - discounted_price / original_price, 2))
                print('This is a ' + str(sale_procentage) + '% sale!\n')

            # Enter a new message for the server or exit
            message = input('Enter another game or "exit" to exit: ')
            if message == 'exit':
                break
    except socket.error:
        print('Socket exception occured!')
        print('The error is ' + str(socket.error))
    finally:
        s.close()

if __name__ == '__main__':
    main()
