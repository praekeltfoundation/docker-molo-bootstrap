ARG PYTHON_TAG=py2
FROM praekeltfoundation/django-bootstrap:${PYTHON_TAG}

# Install gettext for translations
RUN apt-get-install.sh gettext

ARG VERSION=5
COPY requirements/${VERSION}.txt requirements/common.txt /requirements/
RUN pip install -r /requirements/${VERSION}.txt -r /requirements/common.txt

ENV PROJECT_ROOT /app/
