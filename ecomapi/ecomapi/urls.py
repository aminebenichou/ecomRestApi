"""
URL configuration for ecomapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from ouedkniss import views
from rest_framework import routers



router = routers.DefaultRouter()
#router.register('Clientsignup', views.ClientView, basename='client signup'),
#router.register('Sellersignup',views.SellerView,basename='seller register'),
#router.register('login',views.loginView,basename="log in "),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  
    path('sellersignup/',include(router.urls)),
    path('login',include(router.urls)),
    #path('rest-auth/', include('rest_auth.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),
    #path('rest-auth/', include('rest_auth.urls')),
] 

