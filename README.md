# Diabetes-prediction
A Django web app deployed on AWS that predicts whether a female has diabetes based on the inputs given using a Support Vector Machine.

![image](https://user-images.githubusercontent.com/65301406/229080630-a382f5d7-8062-4453-bd18-a18522e04dab.png)

## How to use:
Step 1: Enter the [website](http://3.104.223.120:8000/)

Step 2: Enter the inputs for the user and click the submit button

Step 3: A window will pop up to show the values that you keyed in followed by the prediction

### Database

You can view past entries in the `DB` tab

![image](https://user-images.githubusercontent.com/65301406/229080559-d98cad9d-facd-4069-86e0-3b072d0d274a.png)

## Docker:

I have also created a Docker repo to store this app. The repo can be found [here](https://hub.docker.com/r/anchengyang/diabetes-django)

### Step 1

Go to Docker Hub and create an [account](https://hub.docker.com/)

### Step 2

Go to my [repo](https://hub.docker.com/repository/docker/anchengyang/diabetes-django/general) and pull the docker image with the following command in your terminal

`docker pull anchengyang/diabetes-django`

The docker image should be pulled and you can verify by entering `docker images` in your terminal to view your images

### Step 3

Run the docker image by running this command in the terminal

`docker run -p 8000:8000 anchengyang/diabetes-django:latest`

### Step 4

Open a new window in your browser and go to `http://localhost:8000/` to launch the django application!

OR

Go to Docker Desktop and open your running container!
