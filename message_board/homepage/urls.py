from django.urls import path
from . import views
from . models import Post

app_name = 'homepage'
urlpatterns = [
    # ex: /polls/
    path('', views.homepage, name='homepage'),
    path('create_post/',views.create_post),  
    path('<int:post_id>/',views.post_details,name="post_details"),
    path('search/',views.search,name="search")
]           