# NOTE: This is a development Dockerfile and is intended for use with the
# molo.core source repository. A built molo.core wheel is expected to exist in
# the dist/ directory.
FROM praekeltfoundation/django-bootstrap:py2

# Install gettext for translations
RUN apt-get-install.sh gettext

COPY dist/molo.core-*.whl requirements/common.txt /requirements/
RUN pip install /requirements/molo.core-*.whl -r /requirements/common.txt

ENV PROJECT_ROOT /app/
