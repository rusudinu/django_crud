<h1 align="center">Hi 👋, welcome to a CRUD Projects app, written in Python, created by Rusu Dinu Ștefan</h1>

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
* Gunicorn
* Kubernetes

# ▶️ Running the app
### On Linux: 
* Install docker (you can read https://docs.docker.com/engine/install/ubuntu/ for more details):   
  1 Update the apt package index and install packages to allow apt to use a repository over HTTPS:  
    &nbsp;&nbsp;&nbsp;&nbsp;1.1 sudo apt-get update  
    &nbsp;&nbsp;&nbsp;&nbsp;1.2 sudo apt-get install \  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;apt-transport-https \  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ca-certificates \  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;curl \  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gnupg-agent \  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;software-properties-common  
  2 Add Docker’s official GPG key: curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -  
  3 Set up the stable repository: sudo add-apt-repository \  
   &nbsp;&nbsp;&nbsp;&nbsp;"deb [arch=amd64] https://download.docker.com/linux/ubuntu \  
   &nbsp;&nbsp;&nbsp;&nbsp;$(lsb_release -cs) \  
   &nbsp;&nbsp;&nbsp;&nbsp;stable"  
  4 Update the apt package index, and install the latest version of Docker Engine and containerd  
    &nbsp;&nbsp;&nbsp;&nbsp;4.1 sudo apt-get update  
    &nbsp;&nbsp;&nbsp;&nbsp;4.2 sudo apt-get install docker-ce docker-ce-cli containerd.io  
  5 Check if docker is installed with: sudo docker --version  
* Creating the Docker image:  
  1 Use a pre-built Docker image:  
    &nbsp;&nbsp;&nbsp;&nbsp;1.1 The image will be pulled from: https://hub.docker.com/r/codingshadows/python_django_crud  
    &nbsp;&nbsp;&nbsp;&nbsp;1.2 sudo docker run -p <HOST_PORT>:8000 codingshadows/python_django_crud:latest  
  2 Or create your own image from the source code:  
    &nbsp;&nbsp;&nbsp;&nbsp;2.1 cd into the project root directory  
    &nbsp;&nbsp;&nbsp;&nbsp;2.2 sudo docker build .  
    &nbsp;&nbsp;&nbsp;&nbsp;2.3 You should get a message like: Successfully built <CONTAINER_ID>  
    &nbsp;&nbsp;&nbsp;&nbsp;2.4 sudo docker run -p <HOST_PORT>:8000 <CONTAINER_ID>  
    
<HOST_PORT> can be any open and available port number. You will use it to connect to the website locally, by entering localhost:<HOST_PORT> in the browser.  

### On Windows:
* read https://docs.docker.com/docker-for-windows/  
