from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
]


def trigger_error(request):
    """ Fonction appeler lors et qui va permettre de tracer l'erreur par Sentry"""
    division_by_zero = 1 / 0


urlpatterns += [
    path('sentry-debug/', trigger_error),
]
