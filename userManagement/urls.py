"""
URL configuration for morimori project.

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
from django.urls import path
from .views import dailyFunc, accountfunc, indexfunc, signupfunc, loginfunc, logoutfunc, listFunc

# app_name= 'userManagement'
urlpatterns = [
    path('index/', indexfunc, name='index'),
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('daily/<int:pk>', dailyFunc, name='daily'),
    path('daily/', dailyFunc, name='daily'),
    path('account/', accountfunc, name='account'),
    path('logout/', logoutfunc, name='logout'),
    path('list/', listFunc, name='list')
]
