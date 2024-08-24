# Steam sale store scraper
This documentation is for running the application locally.

The documentation goes over:
- What is the app;
- Creation and structure;
- Installation;
- Start and use.


## What is the app
The "Steam sale store scraper" (`Ssss` like a snake) is a client-server multithread web scraper made with Python3. It's main purpose is for the user to check what's the current price of a game in the Steam online marketplace.

## Creation and structure
As it was said above the application is made in Python3, using libraries that come with the language and some that need to be downloaded additionally. The libraries that come with the language are **socket**, **pickle** and the library used for working with threads. These are mainly used to handle the connection between the client and the server. Where the server creates a thread for each connection and uses sockets to send and receive information from the client.
	The libraries that need to be installed from the `requirements.txt` file are **requests**, **beautifulsoup4** and **lxml**. Each of these is used to handle the web scraping part of the application. Using the *requests* library we get the page from the chosen url of a site. Then a *BeautifulSoup* object is created with that page's text parsed into *lxml*. After this the required information for a game is scraped and send back to the client to be displayed.
	In this case the information that the client requests is the price of a game. The application goes to the *Steam* store page and gets the first entry in a list of the search results. The *Steam* store's first entry in the result list is the closest title to the one the client asked for.
## Installation
To start using the app you only need to install the required libraries from the `requirements.txt` file and have `python3`.
If you don't have `python3` installed follow a tutorial to install it on your OS.
After `python3` is installed it's as easy as running:

	pip install -r requirements.txt

If you are using an Arch based Linux distribution installing things with pip gives an error. To circumvent this issue run:

	pip install -r requirements.txt --break-system-packages

## Start and use
Since this is a client-server application at the moment there are two programs that need to be run.
### Server:
First the server needs to be turned on. To do that simply run:

	python3 server.py

Afterwards the program should print:

	Server binded to port: 12123
	Server is listening for connections...

This meas that the server is working correctly.

### Client:
The client can be run from as many instances as one likes. For this example we assume that only one client will be run since the server works only locally. To start the client simply run:

	python3 client.py

Then the client side app should ask the user for a game name and the server should say:

	Connected to address: 127.0.0.1 : XXXXX

where `XXXXX` is some integer.
If that's the case the app can now be used freely for any request the user has.
### Use:
To search for a game type it's name. After a game is found the title will also be displayed to correct any errors that might occur on the user's part.
To stop the client application type `exit` on the client side. Stopping the server requires the `Ctrl+C` shortcut.
