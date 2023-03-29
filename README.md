# Introduction
This project is about the development and operationalisation of a data-based appplication.


# File Path Navigation
## python_survey_app\script1.py 
The main read script responsible for running the input application.
## python_survey_app\script2.py
The main read script responsible for running the output application.
## python_survey_app\csvhelper\__init__.py 
The write script containing 7 functions correlating to the 7 application requirements.
## python_survey_app\test_app.py 
The test script containing 26 test cases to test all 7 functions from the write script.

# Docker Instructions
Navigate to the folder where the mvtools.Dockerfile exists.

## Build Container 
docker build --rm -t mvtools -f mvtools.Dockerfile .

## Run container in terminal
docker run --rm -it --mount type=bind,target=//root/code,source=/"$(pwd)" mvtools

## Exit container
exit
