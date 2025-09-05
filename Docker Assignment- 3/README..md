# Docker Assignment 3

### Use docker to deploy a containerize version of node.js application. the application should use theficial node.js image and install the required dependences for that configure the container to use volume to persistent data. 


### Node.js Application

- Switch to root user
``` 
sudo su -
```
- Update Operating system
```
apt update
```
- Install docker
``` 
apt install docker 
```
- Start and enable docker
```
systemctl start docker
systemctl enable docker
```
- Install npm package
```
apt install npm -y
```
```
npm -v
```
  
- Create a project directory:

```
mkdir <anyname> 
cd <directory_name>
```

- Initialize Node.js and install a dependency, for example Express:

```
npm init -y
```
```
npm install express
```

- Create file `app.js` with sample code:
[Click here to view app.js code](https://github.com/Mayurhatte09/docker-projects/blob/main/Docker%20Assignment-%203/app.js)

### Create a Dockerfile

- Add a `Dockerfile` to your project folder:

```dockerfile
FROM node:18
WORKDIR /mnt
COPY package.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["node", "app.js"]
```

- Build the Docker Image
```
docker build -t node-app .
```


- Create folder for Volume
```
mkdir -p /my-volume
```
- Build container from docker image
```
docker run --name <Container_name> -p 3000:3000 -v /my-volume -it <Image_Id>
```
- Restart container
```
  docker restart <container_id>
```
`docker ps` listout your runnig contioner
`docer inspect <container_ID>` check volume source

## Check Deployment
- Open your browser and paste this command
```visit
http://localhost:3000
```
```visit
<Instance_public_Ip>:3000
```
---
*You see your app is running.*
---




