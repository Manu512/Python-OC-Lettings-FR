import os

import pytest

from oc_lettings_site.settings import local


@pytest.fixture(scope='session')
def django_db_setup():
    local.DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(local.BASE_DIR, 'oc-lettings-site.sqlite3'),
        }
    }
