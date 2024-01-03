# scrape_store
A web scraper server-client application made with Python for a DevOps and Network programming courses in FMI.

# Cheatsheet
### Run with docker compose

- Build with command in the main directory:

        sudo docker compose build

- Create a network for the containers to connect to:

        sudo docker network create server-client-network

- Run the app from containers
This requires two terminals: one for the client and one for the server.
Start the server with:

        sudo docker run -it --network=server-client-network scrape_store-server

- Start the client with:

        sudo docker run -it --network=server-client-network scrape_store-client
