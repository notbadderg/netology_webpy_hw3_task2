# Building the image
```docker image build <path_to_Dockerfile_dir>```


# Running a container
- Using default ENV vars:
```
$ docker run -d --rm -p <host_port>:8000 --name <container_name> <image_name>
```
- Using specified ENV vars:
```
$ docker run -d --rm -p <host_port>:8000 -e SECRET_KEY=<secret_key> -e DEBUG=<debug> -e ALLOWED_HOSTS=<allowed_hosts> --name <container_name> <image_name>
```
- Using specified ENV file (see env.list.example):

```
$ docker run -d --rm -p <host_port>:8000 --env-file env.list.example --name <container_name> <image_name>
```