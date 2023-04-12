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