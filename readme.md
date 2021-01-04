## Coding Challenge (Django) - Job Portal

### Overview
A simple job portal website created using Python and Django web framework where users/applicant can register for an account, fill in personal and professional information and attach application documents. This app will also notify users via email on initial account registration as well as profile submission.


### Technology Stack

 - Python 3.6
 - Django 3.1
 - SQLite3 / MySQL

### Getting started

Existing Python installation is required.

Download or pull the project files from this repository.

It is recommended to isolate this project from the other projects on the system by creating a separate virtual environment using venv. This can be done by using the following command.

    # cd to main project directory
    cd Coding_Challenge_Django
    
    # create new virtual environment
    venv venv

    # activate venv
    venv\Scripts\activate

    # install required dependencies
    pip install -r requirements.txt

### Modify email settings

To enable/use email notification functionality, the following variables should be supplied with appropriate values:

    # job_application_portal/job_application_portal/settings.py

    DEFAULT_FROM_EMAIL = 'do_not_reply <do_not_reply@jobportal.com>'
    EMAIL_HOST_USER=email@jobportal.com
    EMAIL_HOST_PASSWORD=emailpassword


### Firing up the development server

Once the virtual environment is activated  and the necessary project dependencies are installed, the backend server can now be fired up using the following command:
   
    python manage.py runserver

This will run the django developement server on default port `8000`.
