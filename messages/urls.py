from django.urls import path
from . import views

app_name = 'messages'

urlpatterns = [
    path('', views.home, name='home'),
    path('api/random-message/', views.get_random_message, name='random_message'),
]
