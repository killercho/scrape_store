'''
Final form of the server part for the server-client web scraper application.
In this form after the server establishes connection and receives the information from the client
the server is expected to run the web scraper and return the appropriate prices for the
requested game.
The search is all connected to the steam search. It will return the value for the game
that is closest to the user search. In the odd case that no such games are found the server
returns [-1, -1] to indicate that the client made a mistake.
If the searched game is actually "Free to play" then the server returns [0, 0].
'''

# Impoting all necessary modules and libraries
import socket, pickle
import requests
from _thread import *
from bs4 import BeautifulSoup, ResultSet

# Constants
TRANSFER_SIZE = 1024
URL = 'https://store.steampowered.com/search/?term='

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
        game_name: str = str(data.decode('ascii'))

        # Create the necessary request url and request it
        game_request: str = '+'.join(game_name.split()).lower()
        page: requests.Response = requests.get(URL + game_request)

        # Create a BeautifulSoup object to be searched
        soup: BeautifulSoup = BeautifulSoup(page.text, 'lxml')

        # Search if there were titles found
        # If there is atleast one title that is the searched title
        # Else no games were found
        game_names_found: ResultSet = soup.find_all("span", class_="title")
        response_value: list[str] = ["-1", "-1"]
        game_name_found: str = "No games found"
        if len(game_names_found) > 0:
            game_name_found = game_names_found[0].get_text()

            # Grab all divs that correspond to a value of the game
            combined_prices_div = soup.find_all("div", class_="discount_prices")[0]
            all_divs_arr = combined_prices_div.find_all("div")

            if len(all_divs_arr) == 2:
                # If the game has two divs with values then it is discounted
                original_value: str= all_divs_arr[0].get_text()
                discounted_value: str = all_divs_arr[1].get_text()
                response_value = [original_value, discounted_value]
            elif len(all_divs_arr) == 1:
                # If the game has one div then it is either free or not discounted
                value = all_divs_arr[0].get_text()
                if value == "Free":
                    response_value = ["0", "0"]
                else:
                    response_value = [value, value]


        # Send the data back to the client with pickle to encode it
        conn.send(pickle.dumps([game_name_found, response_value]))
    conn.close()


def main() -> None:
    HOST = ''
    PORT = 12123

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
