# Run distro as a base
FROM alpine

# Run the install and update commands
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python

# Copy all the necessary files and install requirements
COPY client.py /usr/

EXPOSE 12123

# Run the app
CMD ["python3", "/usr/client.py"]
