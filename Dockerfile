FROM praekeltfoundation/django-bootstrap:py2

# Install gettext for translations
RUN apt-get-install.sh gettext

COPY requirements/common.txt /requirements/
RUN pip install -r /requirements/common.txt

ARG VERSION=6
COPY requirements/${VERSION}.txt /requirements/
RUN pip install -r /requirements/${VERSION}.txt

ENV PROJECT_ROOT /app/
