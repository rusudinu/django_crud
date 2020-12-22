<h1 align="center">Hi 👋, welcome to a CRUD Projects app, written in Python [ +Django ], created by Rusu Dinu Ștefan, also known as DDDECAR</h1>

# ❓ Project Description

This is a simple CRUD app, that displays all the projects that I made in the past, and allows me to add, delete and
update the projects in the database. You should be able to play with the app at: https://rusu.dev.codingshadows.com

# 📋 Technical documentation

## 🧰 Frameworks / Tools used

* Python
* Django
* SQlite3
* Docker
* Nginx
* Kubernetes

# ▶️ Running the app
### On Linux: 
* Install docker: 
  1 Update the apt package index and install packages to allow apt to use a repository over HTTPS:
    1.1 sudo apt-get update
    1.2 sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
  2 Add Docker’s official GPG key: curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
  3 Set up the stable repository: sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
  4 Update the apt package index, and install the latest version of Docker Engine and containerd
    4.1 sudo apt-get update
    4.2 sudo apt-get install docker-ce docker-ce-cli containerd.io
  5 Check if docker is installed with: sudo docker --version
* Creating the Docker image:
  1 Use a pre-built Docker image:
    1.1 The image will be pulled from: https://hub.docker.com/r/codingshadows/python_django_crud
    1.2 sudo docker run -p <HOST_PORT>:8000 codingshadows/python_django_crud:latest
  2 Or create your own image from the source code:
    2.1 cd into the project root directory
    2.2 sudo docker build .
    2.3 You should get a message like: Successfully built <CONTAINER_ID>
    2.4 sudo docker run -p <HOST_PORT>:8000 <CONTAINER_ID>
    
<HOST_PORT> can be any open and available port number. You will use it to connect to the website locally, by entering localhost:<HOST_PORT> in the browser.

### On Windows:
* read https://docs.docker.com/docker-for-windows/
