web: python manage.py migrate --settings=recipe_project.settings.prod && gunicorn --env DJANGO_SETTINGS_MODULE=recipe_project.settings.prod recipe_project.wsgi --log-file - && python3 manage.py collectstatic --settings=recipe_project.settings.prod

