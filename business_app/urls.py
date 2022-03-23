"""business_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from business_game import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('business_page', views.business_page, name='business_page'),
    path('business_creation_page', views.business_creation_page, name='business_creation_page'),
    path('location_page_london', views.location_page_london, name='location_page_london'),
    path('location_page_glasgow', views.location_page_glasgow, name='location_page_glasgow'),
    path('business_app/', include('business_game.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
