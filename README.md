# Diagnostic Test Recommender Web Application

## Motivation behind this project
1. While working on real world projects or ideas, we spend a lot of time on tasks like project setup, cicd pipeline set up, deployment, documentation than on the actual implementation of our idea.
2. This project provides you a boiler plate project template for a Django Webapplication with all the necessary things built in.
3. All you need to do is download this code base and follow a few simple steps to get it running on your machine or on AWS.
4. Then you can extend the logic inside this already deployed project to suit your needs.

## What does this project do
1. This is a ready to go Django Web Application project template.
2. It has a complete CICD pipeline using GitHub Actions
3. The CICD Pipeline includes, linting, testing and deployment.
4. The project can be deployed locally as well as to the cloud like AWS or any other cloud servide.
5. It consists of html/css website that are responsive to multiple screen sizes.
6. The website is not very complex and can be easily extended to suit your needs.

## Real World Application of this project
This website first takes in a persons basic information, some information about their habits, their personal & family health history. it then uses this information to recommend a personlaised suite of diagnostic tests that the patient should get done. For someone who has already given this information, it will pull their previous responses, allow them to make any changes and then recommends the tests based on this information.

## Technologies used in this project
1. Python :  The programming language we will be using.
2. Django : We will be using Django on top of the Python framework. It's basically a Python framework for building websites.
3. Django Rest Framework : It adds features for building rest APIs. We will install this into Django.
4. Sqllite : Sqllite will be the database we will be using to store data.
5. We will be using the Djanto Test Framework for the Unit Tests
6. We will be using Flake8 for Code Linting.
7. GitHub Actions : So GitHub actions is going to handle the CICD part. So it'll be used to run things like testing and linting every time we make changes to our code and push the code up to GitHub.


## Django Project Structure
1. app/ : This is the main folder that consists of the Django project and apps
2. app/app/ : This is the Django project
3. app/module/ : This is one of the Django apps that consists of most of the business logic of our web application

## Contents of this code base
This code base as mentioned above is a Django REST API application.
It has the following folders at the root level :
1. .github/workflows -  This is a yaml configuration file is used by github actions for the cicd pipeline. We define what actions we want github to run when we push code to the master branch.
2. app folder - This contains all of the Django project files. It consists of the the multiple django apps we define for our application. It has the following contents:
    - manage.py : It is command-line utility for Django projects. It is generated automatically. It is placed in the root directory of the current project. It sets the DJANGO_SETTINGS_MODULE environment variable to point to the project’s settings.py file.
    - app : This is the main Django app folder that consists of the main Django files like settings.py, the urls that are exposed , the swagger documentation url etc..
        - __init__.py : the __init__.py file is used to mark a directory as a Python package. it comes by default when you create a Django project
        - asgi.py : As well as WSGI, Django also supports deploying on ASGI, the emerging Python standard for asynchronous web servers and applications. Django’s startproject management command sets up a default ASGI configuration for you, which you can tweak as needed for your project, and direct any ASGI-compliant application server to use.
        - settings.py : The settings.py file is the central one for configuring all Django projects. It is nothing else than a Python module with defined variables. All variables inside are constants, and according to PEP 0008 convention, they should be written with capital letters.
        - urls.py : This is the entry point for the project. Contains the root URL configuration of the entire project
        - wsgi.py : It is mostly used during deployment. It is used as an interface between application server to connect with django or any python framework which implements wsgi




## Setup
This section will do the following:
1. Set up your system with the necessary software needed
2. Set up the project
3. Set up the CICD pipeline
Once the above is done, you will be able to build & deploy your project.

### System Setup
1. Install a code editor. I used VSCode
2. Install Docker Desktop for Windows or Mac
    - Once you are done installing, run the below commands to verify the install.
    - Run docker --version
    - Run docker-compose --version
3. Install Git
    - Most machines already come with git installed but since we are using Github actions for the CICD pipeline, you will need to ensure that git is installed.

### Project Setup
**Git**
1. Go to your github account and create a repository. Copy the https or ssh url for your project.
2. Then on your local machine, go to the location where you want to clone the repository
3. Run git clone "url for the project".


**Python Requirements**
1. All the python requirements are listed in the requirements.txt.
2. We also have a requirements.dev.txt in which we list the dependencies that are needed only during development.
3. Later you will see that in the Dockerfile, when we are running the project for the dev environment, we also install the dependencies mentioned in the requirements.dev.txt.
4. Since we already cloned the code base, we already have the requirements.txt and requirements.dev.txt file.
5. **_Depending on when you are using this, the versions for some of these dependencies might need to be updated to the latest versions._**


**Linting & Tests**
1. As you might have seen , we use flake8 for linting and this has already been included in the requirements.dev.txt
2. For testing we use the Django test framework that comes with Django.

**GitHub Actions Configuration**
1. The .github/workflows/checks.yml contains the configuration for GitHub Actions.
2. But essentially we set set up a trigger and then steps for linting and testing.
3. We also set up DockerHub authentication using the secrets we created in the settings of our github repo earlier.
4. While its not necessary to set up DockerHub authentication, it gives us the advantage of getting around the rate limits set by docker to pull the base images each time we build our image.
2. The file has detailed comments for each step which you can go through tio get a better understanding of what happens in the file.


## Django Admin
1. Once you run the project, you will need to create a superuser to login to the Django Admin Module.
2. Run ```docker-compose -f docker-compose-deploy.yml run --rm app sh -c "python manage.py createsuperuser"``` to create a superuser.
3. Navigate to ```http://127.0.0.1:8000/admin/login/?next=/admin/``` to access the admin page.
4. Login with the superuser login and password.
5. The Django Admin Module will load. You will be able to manage users, authentication & the entities you created in the project i.e diagnostictests & tags in this case.

## Interacting with the Website




## Build & Deploy this project to the AWS Cloud
### Cloud Deployment Process Summary


### AWS Setup





### Accessing the Website Post Deployment to AWS




## Misc Topics

