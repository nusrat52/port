python3 manage.py makemigrations --no-input
python3 manage.py migrate --no-input
python3 manage.py collectstatic --noinput
python3 manage.py runserver 0.0.0.0:8000 