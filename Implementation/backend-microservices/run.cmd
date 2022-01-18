cd api-management-system
mkdir ams
cd ..

docker-compose build 
docker-compose run --rm ams sh -c 'django-admin startproject ams .'
docker-compose run --rm ams sh


docker-compose run --rm ams sh -c 'python manage.py test && flake8'
docker-compose run --rm ams sh -c 'python manage.py flake8'

docker-compose run --rm ams sh -c 'python manage.py startapp core'
docker-compose run --rm ams sh -c 'python manage.py makemigrations'
docker-compose run --rm ams sh -c 'python manage.py startapp auth'
