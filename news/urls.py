# from django.conf.urls import url
from . import views
from django.urls import path, re_path



urlpatterns = [
  path('', views.news_today, name='todayNews'),
  re_path('^archives/(\d{4}-\d{2}-\d{2})/$', views.past_days_news, name = 'pastNews'),
  re_path('^search/$', views.search_results, name='search_results'),

]