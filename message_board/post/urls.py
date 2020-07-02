from django.urls import path
from . import views
from .models import Post

app_name="edit_post"
urlpatterns=[
    path('<int:post_id>/',views.post_details,name="post_details"),  
    path('create_post/',views.create_post),
    path('edit_post/<int:post_id>',views.edit_post),
    path('delete_post/<int:post_id>/',views.delete_post),
    path('edit_post/<int:post_id>/',views.edit_post)
]
