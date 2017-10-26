from django.conf.urls import url
from . import views
from .views import DataView, index

urlpatterns =  [
    url(r'^$', views.index, name='index'),
    url(r'^charts/$', DataView.as_view(template_name = 'chart.html')),

]