# Run distro as a base
FROM alpine

# Run the install and update commands
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN apk add py3-pip
#RUN python3 -m ensurepip

# Copy all the necessary files and install requirements
COPY server.py /usr/
COPY requirements.txt /usr/
RUN pip3 install -r /usr/requirements.txt --break-system-packages

EXPOSE 12123

# Run the app
CMD ["python3", "/usr/server.py"]
