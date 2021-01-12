ARG PYTHON_TAG=py3.6-stretch
FROM praekeltfoundation/django-bootstrap:${PYTHON_TAG}

# Install gettext for translations
RUN apt-get-install.sh gettext

ARG VERSION=11
COPY requirements/${VERSION}.txt requirements/common.txt /requirements/
RUN pip install -r /requirements/${VERSION}.txt -r /requirements/common.txt

ENV PROJECT_ROOT /app/
