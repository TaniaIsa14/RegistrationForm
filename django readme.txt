pip install django
django-admin startproject project1
cd project1
python manage.py startapp myapp
python manage.py migrate
python manage.py create superuser

python manage.py runserever