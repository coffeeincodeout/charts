from django.conf.urls import url
from .views import DataView
from . import views


urlpatterns =  [
    url(r'^$', views.index, name='index'),
    url(r'^charts/$', DataView.as_view(template_name = 'chart.html')),
    #url(r'^companies_api/', views.BusinessProfileList.as_view()),
]

