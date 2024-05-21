# SAWAABA-CELERY

This is a website application to purchase air-ticket, rent hotel rooms and cars.

This is a Python-Django project with PostgreSQL database.

Python version - 3.11.7
Django version - 5.0
Postgres version - 16

git fetch && git checkout 240310-modify-models-sandbox

git add .        
git commit -m "240310 - add member cruds"   
git push -u origin  

touch .gitignore 
python manage.py createsuperuser

find / -type d -name "venv" 2>/dev/null

/usr/local/Cellar/python@3.12/3.12.3/Frameworks/Python.framework/Versions/3.12/lib/python3.12/venv
/usr/local/Cellar/python@3.10/3.10.11/Frameworks/Python.framework/Versions/3.10/lib/python3.10/venv
/usr/local/Cellar/python@3.11/3.11.7_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/venv
/usr/local/Cellar/python@3.8/3.8.16/Frameworks/Python.framework/Versions/3.8/lib/python3.8/venv
/usr/local/Cellar/python@3.9/3.9.16/Frameworks/Python.framework/Versions/3.9/lib/python3.9


pip install virtualenv
virtualenv venv
source venv/bin/activate
python virtual_env.py   
pip install requests
deactivate

pip install -r requirements.txt

pip install dj-database-url
pip install gunicorn
gunicorn SAWAABA.wsgi
pip install 'whitenoise[brotli]'
pip install gunicorn uvicorn
pip install django-celery-results
python manage.py migrate django_celery_results
pip install python-dotenv
pip install django-countries
pip install --upgrade django_countries
pip install django-appointment
pip install psycopg2
pip install pyfcm
pip install twilio
pip install paypalrestsdk




chmod a+x build.sh
python -m gunicorn SAWAABA.asgi:application -k uvicorn.workers.UvicornWorker

python3 manage.py makemigrations travel
python3 manage.py migrate 
python3 manage.py seed_quran

python3 manage.py runserver              
python3 manage.py check

pip freeze > requirements.txt

brew update  
brew install rabbitmq 
export PATH=$PATH:/usr/local/sbin
brew services start rabbitmq
pip install celery
celery.py > add and copy paste codes
celery -A SAWAABA worker -l info
celery -A SAWAABA beat --loglevel=info


<!-- https://docs.render.com/deploy-django -->
<!-- https://www.youtube.com/watch?v=wczWm8j4v9w -->
<!-- pip install celery -->
<!-- brew install rabbitmq -->
<!-- brew reinstall rabbitmq  -->
<!-- brew services list -->
<!-- brew services info rabbitmq -->
<!-- rabbitmq-server start -->
<!-- brew services stop rabbitmq -->
<!-- brew services disable rabbitmq -->
<!-- brew services start rabbitmq -->
<!-- brew services restart rabbitmq -->
<!-- celery -A SAWAABA worker --loglevel=info -->
<!-- celery -A SAWAABA beat --loglevel=info -->

<!-- pip install django-scheduler -->
<!-- pip freeze -->
<!-- python manage.py makemigrations -->
<!-- python3.11 manage.py migrate schedule -->
<!-- https://django-scheduler.readthedocs.io/en/latest/install.html -->


<!-- pip install django-appointment -->
<!-- http://127.0.0.1:8000/appointment/app-admin/appointments/ -->
<!-- https://pypi.org/project/django-appointment/ -->
<!-- https://github.com/adamspd/django-appointment/blob/main/docs/explanation.md -->

<!-- pip install twilio -->

<!-- source /home/pftit276/virtualenv/sawaaba/travel/templates/travel/3.11/bin/activate && cd /home/pftit276/sawaaba/travel/templates/travel -->
