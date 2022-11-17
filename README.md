# Paul the Octopus

A basic project to use for the Paul the Octopus challenge (World Cup 2022) written in Python and using GCP platform. 

It makes match predictions using the FIFA ranking and historical results of the two teams. 


## Requirements

The datasets and historical data are stored in BigQuery tables and CSV files on GCP platform. 


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
   > python3 main.py <year>

   It is mandatory to inform the year. If the year is the current year, it will predict the results for the next World Cup (load matches from the csv file). 
   Otherwise, it will load the matches from the World Cup year informed e check the predictions and the official resultas.
       
