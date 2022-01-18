from django.urls import path
from business_game import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'business_game'

urlpatterns = [
    path('', views.index, name='index'),
]