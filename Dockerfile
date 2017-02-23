FROM praekeltfoundation/django-bootstrap:py2

# Install gettext for translations
RUN apt-get-install.sh gettext

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ENV PROJECT_ROOT /app/
