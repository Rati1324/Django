from django.urls import path
from . import views

app_name = 'register'
urlpatterns = [
    # ex: /polls/
    path('register/', views.register, name='register'),
    path('login/',views.login_view, name='login_view'),
    path('logout/',views.logout_view,name="logout")
]           