FROM praekeltfoundation/molo-bootstrap

# Generate a test app and install it
RUN molo scaffold testapp .
RUN pip install -e .

COPY docker_settings.py testapp/settings/docker.py
ENV DJANGO_SETTINGS_MODULE testapp.settings.docker
ENV CELERY_APP testapp

RUN set -ex; \
    django-admin collectstatic --noinput; \
    django-admin compress

CMD ["testapp.wsgi:application"]
