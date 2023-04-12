# jobbee_djangle_next

# Install python virtualenv and necessaries libs

`pip3 install virtualenv`
`virtualenv myenv`
`source myenv/bin/activate`

`pip3 install django`

`pip3 install boto3 django-cors-headers django-dotenv django-filter django-storages djangorestframework djangorestframework-simplejwt geocoder gunicorn whitenoise psycopg2 dj-database-url`

`brew install gdal geos`

# Create Django project

`django-admin startproject backend`

# Create a database in PostgreSQL.
In this project I'm using a database called `jobbee-api`.

# Create VarEnvs

export GDAL_LIBRARY_PATH=/opt/homebrew/lib/libgdal.dylib 

export GEOS_LIBRARY_PATH=/opt/homebrew/lib/libgeos_c.dylib

# Run the initial migrations
`python3 manage.py migrate`

# Create superuser to admin Djangle
`python3 manage.py createsuperuser`

# Start project
`python3 manage.py runserver`


# Created app job
python3 manage.py startapp job

# Modified models.py Jobs


# Create account and get the key from Geocoder
https://developer.mapquest.com/user/me/profile

# 12. Run Migrations & Create first Job

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver

## On the webpage, created a new job
http://localhost:8000/admin


# Get data from Insomnia
http://localhost:8000/api/jobs/


# Get Stats of Topic
Insert job titles with java description, for example, and filter like this:

http://localhost:8000/api/stats/java
http://localhost:8000/api/stats/python
