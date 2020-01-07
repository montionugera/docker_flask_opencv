# Python Flask Opencv Dockerized Application#

Build the image using the following command

```bash
$ docker build -t flask-opencv:latest .
```

Run the Docker container using the command shown below.

```bash
$ docker run -d -p 5000:5000 flask-opencv
```

The application will be accessible at http:127.0.0.1:5000 or if you are using boot2docker then first find ip address using `$ boot2docker ip` and the use the ip `http://<host_ip>:5000`
