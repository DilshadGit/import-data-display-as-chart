from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^summary/', views.summary, name='summary'),
    url(r'^detail/', views.detail, name='detail'),
    url(r'^api/data/', views.get_data_from_store, name='api-data'),
    url(r'^api/chart/data/', views.ChartData.as_view()),
]