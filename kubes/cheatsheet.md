# Starting the app from Kubernetes in a local setting

## Installation and preparation
To start the application from a Kubernetes cluster you need to first start the minikube app with:

	minikube start

If an error occurs with the starting, then follow the instructions provided in the output log of the command.

## Starting the service
To start the server service:
 - go into the root of the project;
 - run `minikube kubectl -- apply -f kubes/` to start the necessary pods;
 - check if the pod is running with `minikube kubectl -- get all`;
 - get the URL of the service to access the IP address with `minikube service --url server-service`

## Launch the client application
After you copy the IP address and the PORT of the server, launch the client application with:

	python3 client/client.py ADDRESS PORT

Where the ADDRESS is the IP address of the server service and the PORT is the port of the server service.
If it all goes according to plan the client should ask for a game.

## Stop the service
When you are ready to stop the service simply type

	minikube stop
