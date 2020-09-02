release: python manage.py migrate --no-input
web: gunicorn --bind :$PORT --workers 4 StackFlow.wsgi:application
