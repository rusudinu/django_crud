<h1 align="center">Hi 👋, welcome to a CRUD Projects app, written in Python [ +Django ], created by Rusu Dinu Ștefan, also known as DDDECAR</h1>

# ❓ Project Description

This is a simple CRUD app, that displays all the projects that I made in the past, and allows me to add, delete and
update the projects in the database.

# 📋 Technical documentation

## 🧰 Frameworks / Tools used

* Python
* Django
* SQLITE3

## To run the app, create a Docker container 
### On Linux: 
* install docker: 
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
* in the project root directory: sudo docker build .
* You should get a message like: Successfully built <CONTAINER_ID>
* run sudo docker run -p 8000:8000 <CONTAINER_ID>

### On Windows:
* read https://docs.docker.com/docker-for-windows/
