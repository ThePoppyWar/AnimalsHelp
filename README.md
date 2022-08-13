# AnimalsHelp

A simple web application built with Django Framework.

#Table of contents

General info
Technologies
Features
Setup

#General Info

A web application, that allows users to add volunteers, animals and donations. Technologies:

Python
Django
HTML


#Features:

user authorization (register, activate by e-mail, login, logout)
signing up as a volunteer or doctor
change in the status of animals depending on the adoption process
adding donations of food etc.
user panel
admin panel


#Setup

First you should clone this repository:

    git clone https://github.com/ThePoppyWar/AnimalsHelp.git
    cd AnimalsHelp

To run the project you should have Python 3 installed on your computer. Then it's recommended to create a virtual environment for your projects dependencies. To install virtual environment:

    pip install virtualenv

Then run the following command in the project directory:

    virtualenv venv

That will create a new folder venv in your project directory. Next activate virtual environment:

    source venv/bin/active

Then install the project dependencies:

    pip install -r requirements.txt

Now you can run the project with this command:

    python manage.py runserver

Note in the settings file you should complete your own database settings.
