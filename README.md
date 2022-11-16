# Paul the Octopus

A basic project to use for the Paul the Octopus challenge (World Cup 2022) written in Python. 

It makes match predictions using the FIFA ranking and historical results of the two teams. 

## Getting started

Steps to install and configure the project:

1) Install Python

    https://python.land/installing-python


2) Install dependencies

   > pip3 install -r requirements.txt

3) GCP configuration

    https://cloud.google.com/sdk/docs/install-sdk

    > gcloud install
   
4) GCP credentials

    https://cloud.google.com/docs/authentication/application-default-credentials

    Set the environment variables with your configuration:
    
    > export GOOGLE_APPLICATION_CREDENTIALS=/Users/login/.config/gcloud/application_default_credentials.json

    > export GCLOUD_PROJECT=phoenix-cit


## Execution

   To run as web application (cloud function)
   > functions-framework --target prediction --debug

   http://127.0.0.1:8080/
   
   To run as command line
   > python3 main.py