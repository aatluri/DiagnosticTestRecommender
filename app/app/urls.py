"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

# This is the main urls.py for this Project.
# We define all the urls that need to be exposed from this project.
# The /admin is exposed by default.
# We can also include other paths from this main project
# We also need to include the urls from the other apps in this project eg: like the module app.
urlpatterns = [
    path('admin/', admin.site.urls),
    # Including the urls from the module app. The url patterns which are defined in the module\urls.py then get included
    path('module/', include("module.urls"))
]
