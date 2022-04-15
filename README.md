```bash
git clone https://github.com/drf-mock-response/drf-mock-response_demo.git
cd drf-mock-response_demo
python -m venv venv
source venv/bin/activate
poetry install
python manage.py migrate
DJANGO_SUPERUSER_PASSWORD=1234 python manage.py createsuperuser --noinput --username admin --email email@email.com
python manage.py runserver
```