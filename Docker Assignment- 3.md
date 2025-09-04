
# Use docker to deploy a containerize version of node.js application. the application should use theficial node.js image and install the required dependences for that configure the container to use volume to persistent data. How can I do this assignment.

To complete your assignment of deploying a containerized Node.js application using Docker, follow these structured steps: create your Node.js app, use the official Node.js Docker image, install dependencies, and persist data using Docker volumes.[^1][^2][^3][^4]


### 1. Prepare a Node.js Application

- Swithch to root user
``` 
sudo su -
```
- Upsate Operationg system
```
apt update
```
Install 
- Install docker
``` 
apt install docker 
```

- Create a project directory:

```
mkdir node-docker-app
cd node-docker-app
```

- Initialize Node.js and install a dependency, for example Express:

```
npm init -y
npm install express
```

- Create `app.js` with sample code:

```javascript
const express = require('express');
const app = express();
app.get('/', (req, res) => res.send('Hello from Node.js in Docker!'));
app.listen(3000, () => console.log('Listening on port 3000'));
```


### 2. Create a Dockerfile

- Add a `Dockerfile` to your project folder:

```dockerfile
FROM node:18
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["node", "app.js"]
```

This uses the official Node.js image and installs all dependencies.[^2][^1]


### 3. Build the Docker Image

- Run the following command inside your project folder:

```
docker build -t node-docker-app .
```


### 4. Create a Persistent Volume

- Create a Docker volume to store your data:

```
docker volume create node-app-data
```


### 5. Run the Container with the Volume

- Start the container, mounting the volume. If you want to persist data in a directory called `/usr/src/app/data`, run:

```
docker run -d -p 3000:3000 -v node-app-data:/usr/src/app/data --name node-app node-docker-app
```

Data stored in `/usr/src/app/data` will remain safe even if the container is stopped or removed.[^5][^3]


### 6. Verify the Deployment

- Visit `http://localhost:3000` in a browser. You should see your running app.


## Summary Table

| Step | Command/Config | Description |
| :-- | :-- | :-- |
| Initialize Project | `npm init -y`<br>`npm install express` | Setup Node.js with Express |
| Dockerfile | See above | Use Node.js image \& install deps |
| Build Image | `docker build -t node-docker-app .` | Create Docker image |
| Create Volume | `docker volume create node-app-data` | Persistent storage for app data |
| Run Container | `docker run -d -p 3000:3000 -v node-app-data:/usr/src/app/data node-docker-app` | Start app with data volume |



