<h1 align="center">CRUD demo projects app, written in Python</h1>

# Project Description

This is a simple CRUD app, that displays all the projects that I made in the past, and allows me to add, delete and update the projects in the database. You should be able to play with the app at: https://rusu.rip.wtf [ with SSL ] or http://rusu.dev.codingshadows.com [ no SSL ]. If you want to see the heavier version of this website, you can check https://codingshadows.com

# User documentation

### Introduction

One can navigate the website using the buttons in the menu bar placed at the top of the page. There are 8 main sections of the website, some that are dynamically generated, and some that are static webpages. The static sections are: Home, Work ( Mobile & Web Development ), Honors & Awards, About & Mentions, C ( Create ). The dynamic pages are R ( Read ), U ( Update ), D ( Delete ). Source Code redirects the user to the github page. One can view real projects in the Work ( and subsections of
Work ) and in Honors & Awards. C R U D pages are for dynamic operations on projects ( explained in [CRUD Ops](#crud-ops)).

### CRUD Ops

CRUD Ops stands for Create, Read, Update and Delete operations performed that showcase basic functions of persistent storage and also a user interface that facilitates viewing, searching and changing information.

* C ( Create ): One can create dummy project entries in the SQL database, using the C button from the menu of the website. ( %DOMAIN_NAME%/create/%REQUEST_PARAMS% )
* R ( Read ): One can read dummy project entries from the SQL database, using the R button from the menu of the website. ( %DOMAIN_NAME%/read/%REQUEST_PARAMS% )
* U ( Update ): One can update dummy project entries in/from the SQL database, using the U button from the menu of the website. ( %DOMAIN_NAME%/update/%REQUEST_PARAMS% )
* D ( Delete ): One can delete dummy project entries from the SQL database, using the D button from the menu of the website. ( %DOMAIN_NAME%/delete/%REQUEST_PARAMS% )

### Special functionalities

The website uses request parameters to identify and facilitate the user experience ( aka UX ). Those request parameters are as follows:

* SID - session id : the session id is used to identify user sessions, so that users may not query or modify data in the database that was not intended for them to modify please read [user permissions](#user-permissions) for further info about custom user sessions.
* PID - project id : the project id is used as a key in the database to identify a project object and perform CRUD ops on that object
* SPID - session & project id : the session & project id is used to identify both a session id, and a project id at the same time

### User permissions

Please note that other users may be able to perform CRUD operations on objects that were created by a known SID.

# Technical documentation

### Dependencies

Listed alphabetically. Motivation is written in ( motivation ).

* Django ( rapid development ( princpile ) and DRY ( principle ), quick to prototype )
* Docker ( easier to scale, demonstration purposes )
* Gunicorn ( bridge between NGINX and Django )
* NGINX ( reverse proxy )
* Python ( project requirement )
* SQlite3 ( single-file database, hence portable, prepackaged with Django and SQL database - project requirement )

# Running your own session ( hosting the app )

### On Ubuntu

* Install Docker ( you may read https://docs.docker.com/engine/install/ubuntu/ for more details ):   
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
* Creating the Docker image ( choose either 1 or 2, do NOT do them both ):  
  1 Use a pre-built Docker image:  
  &nbsp;&nbsp;&nbsp;&nbsp;1.1 The image will be pulled from: https://hub.docker.com/r/codingshadows/python_django_crud  
  &nbsp;&nbsp;&nbsp;&nbsp;1.2 sudo docker run -p <HOST_PORT>:8000 codingshadows/python_django_crud:latest  
  2 Create your own image from the source code:  
  &nbsp;&nbsp;&nbsp;&nbsp;2.1 cd into the project root directory  
  &nbsp;&nbsp;&nbsp;&nbsp;2.2 sudo docker build .  
  &nbsp;&nbsp;&nbsp;&nbsp;2.3 You should get a message like: Successfully built <CONTAINER_ID>  
  &nbsp;&nbsp;&nbsp;&nbsp;2.4 sudo docker run -p <HOST_PORT>:8000 <CONTAINER_ID>

### On Debian

* Install Docker ( you may read https://docs.docker.com/engine/install/debian/ for more details ):   
  1 Update the apt package index and install packages to allow apt to use a repository over HTTPS:  
  &nbsp;&nbsp;&nbsp;&nbsp;1.1 sudo apt-get update  
  &nbsp;&nbsp;&nbsp;&nbsp;1.2 sudo apt-get install \  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;apt-transport-https \  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ca-certificates \  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;curl \  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gnupg-agent \  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;software-properties-common  
  2 Add Docker’s official GPG key: curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -  
  3 Set up the stable repository: sudo add-apt-repository \  
  &nbsp;&nbsp;&nbsp;&nbsp;"deb [arch=amd64] https://download.docker.com/linux/debian \  
  &nbsp;&nbsp;&nbsp;&nbsp;$(lsb_release -cs) \  
  &nbsp;&nbsp;&nbsp;&nbsp;stable"  
  4 Update the apt package index, and install the latest version of Docker Engine and containerd  
  &nbsp;&nbsp;&nbsp;&nbsp;4.1 sudo apt-get update  
  &nbsp;&nbsp;&nbsp;&nbsp;4.2 sudo apt-get install docker-ce docker-ce-cli containerd.io  
  5 Check if docker is installed with: sudo docker --version
* Creating the Docker image ( choose either 1 or 2, do NOT do them both ):  
  1 Use a pre-built Docker image:  
  &nbsp;&nbsp;&nbsp;&nbsp;1.1 The image will be pulled from: https://hub.docker.com/r/codingshadows/python_django_crud  
  &nbsp;&nbsp;&nbsp;&nbsp;1.2 sudo docker run -p <HOST_PORT>:8000 codingshadows/python_django_crud:latest  
  2 Create your own image from the source code:  
  &nbsp;&nbsp;&nbsp;&nbsp;2.1 cd into the project root directory  
  &nbsp;&nbsp;&nbsp;&nbsp;2.2 sudo docker build .  
  &nbsp;&nbsp;&nbsp;&nbsp;2.3 You should get a message like: Successfully built <CONTAINER_ID>  
  &nbsp;&nbsp;&nbsp;&nbsp;2.4 sudo docker run -p <HOST_PORT>:8000 <CONTAINER_ID>

### On Raspberry Pi

* Install Docker ( you may read https://docs.docker.com/engine/install/debian/ for more details ):   
  1 Update the apt package index and install packages to allow apt to use a repository over HTTPS:  
  &nbsp;&nbsp;&nbsp;&nbsp;1.1 sudo apt-get update  
  &nbsp;&nbsp;&nbsp;&nbsp;1.2 sudo apt-get install \  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;apt-transport-https \  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ca-certificates \  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;curl \  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gnupg-agent \  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;software-properties-common  
  2 Add Docker’s official GPG key: curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -  
  3 Set up the stable repository: sudo add-apt-repository \  
  &nbsp;&nbsp;&nbsp;&nbsp;"deb [arch=amd64] https://download.docker.com/linux/debian \  
  &nbsp;&nbsp;&nbsp;&nbsp;$(lsb_release -cs) \  
  &nbsp;&nbsp;&nbsp;&nbsp;stable"  
  4 Update the apt package index, and install the latest version of Docker Engine and containerd  
  &nbsp;&nbsp;&nbsp;&nbsp;4.1 sudo apt-get update  
  &nbsp;&nbsp;&nbsp;&nbsp;4.2 sudo apt-get install docker-ce docker-ce-cli containerd.io  
  5 Check if docker is installed with: sudo docker --version
* Creating the Docker image ( choose either 1 or 2, do NOT do them both ):  
  1 Use a pre-built Docker image:  
  &nbsp;&nbsp;&nbsp;&nbsp;1.1 The image will be pulled from: https://hub.docker.com/r/codingshadows/python_django_crud  
  &nbsp;&nbsp;&nbsp;&nbsp;1.2 sudo docker run -p <HOST_PORT>:8000 codingshadows/python_django_crud:latest  
  2 Create your own image from the source code:  
  &nbsp;&nbsp;&nbsp;&nbsp;2.1 cd into the project root directory  
  &nbsp;&nbsp;&nbsp;&nbsp;2.2 sudo docker build .  
  &nbsp;&nbsp;&nbsp;&nbsp;2.3 You should get a message like: Successfully built <CONTAINER_ID>  
  &nbsp;&nbsp;&nbsp;&nbsp;2.4 sudo docker run -p <HOST_PORT>:8000 <CONTAINER_ID>

### On Windows

* Install Docker ( you may read https://docs.docker.com/docker-for-windows/ )
* Creating the Docker image ( choose either 1 or 2, do NOT do them both ):  
  1 Use a pre-built Docker image:  
  &nbsp;&nbsp;&nbsp;&nbsp;1.1 The image will be pulled from: https://hub.docker.com/r/codingshadows/python_django_crud  
  &nbsp;&nbsp;&nbsp;&nbsp;1.2 docker run -p <HOST_PORT>:8000 codingshadows/python_django_crud:latest  
  2 Create your own image from the source code:  
  &nbsp;&nbsp;&nbsp;&nbsp;2.1 cd into the project root directory  
  &nbsp;&nbsp;&nbsp;&nbsp;2.2 docker build .  
  &nbsp;&nbsp;&nbsp;&nbsp;2.3 You should get a message like: Successfully built <CONTAINER_ID>  
  &nbsp;&nbsp;&nbsp;&nbsp;2.4 docker run -p <HOST_PORT>:8000 <CONTAINER_ID>

Notes:  
<HOST_PORT> may be any open and available port number. You will use it to connect to the website locally, by entering localhost:<HOST_PORT> in the browser. The choice of <HOST_PORT> to be 80 is preferred, but not mandatory. If you also run an NGINX proxy in front of the project, you may choose <HOST_PORT> to be other than 80 in order to allow NGINX to listen on port 80.
