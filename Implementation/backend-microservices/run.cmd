cd api-management-system
mkdir ams
cd ..

docker-compose build 
docker-compose run ams sh -c 'django-admin startproject ams .'
