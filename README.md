# Django CRUD Operations
A simple CRUD in django

## Demo
## Technologies used:
* Python v3 programming language
* Django v3 server-side web framework
* Bootstrap v4

## Setup
* Install Python
* Install pip
* Install Django by typing pip install Django
* Run python manage.py startapp new_module to create Python module
* Add code
* Run pip freeze to see list of modules installed. Ref. Docs
* Run python manage.py makemigrations for changes to models etc.
* Run python manage.py migrate to migrate the migration files.

### Running the Application
Before running the application we need to create the needed DB tables:

> ./manage.py migrate

Now you can run the development web server:

> ./manage.py runserver

To access the applications go to the URL http://localhost:8000/

## Need a user and password to access 
Yes, the project demonstrate how CRUD can work with Django users, and you do need to create a user to test it, you can create a user using the following command:

> ./manage.py createsuperuser

## Licence
## Contact
* Repo created by [Maryam Muchai](https://github.com/MaryamMuchai), Email: maryammuchai@gmail.com