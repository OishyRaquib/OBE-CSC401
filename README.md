# OBE-CSC401

## Quick installation
You can setup a virtual environment installing virtualenv and typing the following commands in terminal:

$ virtualenv <folder_name>


Then activate it:
 $ source <folder_name>/bin/activate


(and optionally you can exit from the virtual environment typing: deactivate)
Once made that you can download the project using git or simply downloading it in a zip format and unzip it and go to the main top folder of workshops:


clone the project 
Using pip (inside the virtual environment) install the necessary dependencies with pip from requirements.txt:
 $ pip install -r requirements.txt


We will migrate after setting the database
$ python manage.py migrate 


We will run the default django's web server typing:
$ python manage.py runserver


#Dependencies
-Panda
-Bootstrap (Can use CDN)
