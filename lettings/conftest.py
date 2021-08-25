import os

import pytest

from oc_lettings_site import settings


@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(settings.BASE_DIR, 'oc-lettings-site.sqlite3'),
        }
    }
