#!/bin/bash
python inforce/manage.py makemigrations authentication
python inforce/manage.py makemigrations restaurant
python inforce/manage.py migrate authentication
python inforce/manage.py migrate restaurant
python inforce/manage.py migrate admin
python inforce/manage.py migrate sessions
python inforce/manage.py runserver 0.0.0.0:8000
