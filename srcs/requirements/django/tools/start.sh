#!/bin/sh

sleep 10

if [ -z "$(find /app -mindepth 1 -print -quit)" ]; then
  django-admin startproject django_basic_app
  mv django_basic_app app_backup
  cp -r app_backup/django_basic_app .
  cp app_backup/manage.py .
  rm -rf app_backup
  python manage.py migrate
fi

python manage.py migrate
./create_superuser.sh
python manage.py runserver 0.0.0.0:8000
