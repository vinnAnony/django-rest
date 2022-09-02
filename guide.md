YT tutorial link - https://www.youtube.com/watch?v=c708Nf0cHrs
# Running Server
python manage.py runserver 8000

# Configuring API in django

python manage.py startapp api

Add api to INSTALLED_APPS in settings.py

# Commands

python manage.py makemigrations
python manage.py migrate
python manage.py shell


# Py shell help

Product.objects.create(id=1,name='Mango')