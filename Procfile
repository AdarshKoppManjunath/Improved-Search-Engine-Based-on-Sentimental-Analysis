web: gunicorn search_engine_project.wsgi:application --log-file -
worker: lein run -m python manage.py process_tasks
