# from django.conf.urls import url
from . import views
from django.urls import path, re_path



urlpatterns = [
  path('', views.welcome, name='Welcome'),
  path('today/', views.news_of_day, name='todayNews'),
  re_path('^archives/(\d{4}-\d{2}-\d{2})/$', views.past_days_news, name = 'pastNews')

]