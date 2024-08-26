web: python src/manage.py migrate --settings=src.recipe_project.settings.prod && gunicorn --env DJANGO_SETTINGS_MODULE=src.recipe_project.settings.prod src.recipe_project.wsgi --log-file -
