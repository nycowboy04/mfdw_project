from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^contacts$', views.contact, name='contact'),
    url(r'([^/]*)', views.index, name = 'index'),
]
