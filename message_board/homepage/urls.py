from django.urls import path
from . import views


app_name = 'homepage'
urlpatterns = [
    # ex: /polls/
    path('', views.homepage, name='homepage'),
    path('search/',views.search,name="search")
]           