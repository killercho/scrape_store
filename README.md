# Steam sale store scraper
The documentation goes over:
- Overview;
- Plan and structure;
	- Git branching strategy;
	- Continuous integration;
	- Continuous deployment;
	- Project folder structure;
- Implementation details;
- Installation;
- Local start and use;
	- Start server;
	- Start client;
	- Using the app.


## Overview
The "Steam sale store scraper" (`Ssss` like a snake) is a client-server multi-thread web scraper made with Python3. Its main purpose is for the user to check what's the current price of a game in the Steam online marketplace.

## Plan and structure

### Git branching strategy
To protect from exploits and to always have a working latest version of the app I decided to use a *Feature branch* strategy.

This branching strategy emphasizes on the use of one **master** branch and one or more **feature** branch, enforced with a GitHub rule forbidding the unauthorized push and force push to the **master** branch.
The only way to push to the **master** branch is by a *Pull request* that is accepted by another contributor after checking the code.

The **master** branch holds the latest stable version of the application, whereas the **feature** branch is used for developing new features and fixing existing issues.
Once the code in the *feature* branch is completed it is merged with the **master** branch thus becoming the next stable version. Then the additional branch is deleted and the cycle continues.

Feature branches do not need to be named in a specific way, but it is **preferred** that they use *feature/* or *bug/* as a prefix, followed by a descriptive name of the new code implemented.

### Continuous integration
Whenever pushing to any branch, the *CI* workflow is executed. This workflow consists of:
 - Flake8			- used to check if the new python code is consistent with the agreed upon styles;
 - Markdown-checker - used to lint, syntax validate and detect errors in the new documentation, pushed in the project in the form of a markdown file;
 - Snyk				- used to identify and warn about existing vulnerabilities in the new code, and if such are found, provide a working solution;
 - SonarCloud		- used to analyze the existing code and provide additional quality assurance;
 - Trivy			- after all the other actions finish successfully, then Trivy is used to scan the result server docker image for any vulnerabilities and other issues.

### Continuous deployment
Whenever pushing to the **master** branch, if the *CI* workflow passes successfully, then the *CD* workflow is run.

This workflow is responsible for pushing the docker containers ( *server* ) to Dockerhub and testing a deployment of the application, if the push was successful.

The *server* docker image that is pushed is always with the *latest* tag, because the master branch is supposed to be only for the latest stable version.
Testing the deployment of the app is done by rolling out and then checking if the *server* was deployed.

### Project folder structure
The hole project is composed of:
 - *client* folder - holding the python code responsible for running the client;
 - *server* folder - holding the docker image file, python code for the server application and the requirements for executing the app;
 - *kubes* folder  - holding the information for the Kubernetes deployment;
 - *README.md file - the documentation that you are reading right now.

## Implementation details
As it was said above the application is made in Python3, using libraries that come with the language and some that need to be downloaded additionally.
The libraries that come with the language are **socket**, **pickle** and the library used for working with threads. These are mainly used to handle the connection between the client and the server.
Where the server creates a thread for each connection and uses sockets to send and receive information from the client.
The libraries that need to be installed from the `requirements.txt` file are **requests**, **beautifulsoup4** and **lxml**. Each of these is used to handle the web scraping part of the application.

Using the *requests* library we get the page from the chosen url of a site.
Then a *BeautifulSoup* object is created with that page's text parsed into *lxml*.
After this the required information for a game is scraped and send back to the client to be displayed.
In this case the information that the client requests is the price of a game. The application goes to the *Steam* store page and gets the first entry in a list of the search results.

The *Steam* store's first entry in the result list is the closest title to the one the client asked for.

## Installation
To start using the app you only need to install the required libraries from the `requirements.txt` file and have `python3`.
If you don't have `python3` installed follow a tutorial to install it on your OS.
After `python3` is installed it's as easy as running:

	pip install -r requirements.txt

If you are using an Arch based Linux distribution installing things with pip gives an error. To circumvent this issue run:

	pip install -r requirements.txt --break-system-packages

## Local start and use
Since this is a client-server application at the moment there are two programs that need to be run.

### Start server:
First the server needs to be turned on. To do that simply run:

	python3 server.py

Afterwards the program should print:

	Server binded to port: 12123
	Server is listening for connections...

This means that the server is working correctly.

### Start client:
The client can be run from as many instances as one likes. For this example we assume that only one client will be run since the server works only locally. To start the client simply run:

	python3 client.py 127.0.0.1 12123

Where the first argument is the server IP address of the server and the second argument is the port of the server.
Then the client side app should ask the user for a game name and the server should say:

	Connected to address: client-address : client-port

Where `client-address` is the client's address and `client-port` is again the port of the client.
If that's the case the app can now be used freely for any request the user has.

### Using the app:
To search for a game, type its name. After a game is found the title will also be displayed to correct any errors that might occur on the user's part.
To stop the client application type `exit` on the client side. Stopping the server requires the `Ctrl+C` shortcut.
