"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.http import HttpResponse
from django.shortcuts import render
from core.views import home_view

def home_view(request):
    #mock data for now
    contacts = [
        {"name": "Steve Smith", "email": "alice@example.com", "phone": "555-0192"},
        {"name": "Bob Mark", "email": "bob@example.com", "phone": "555-0143"},
        {"name": "Charlie Douglas", "email": "charlie@example.com", "phone": "555-0188"},
    ]

    context = {
        "contacts": dummy_contacts
    }
    
    return render(request, "home.html", context)

# Simple Hello World view function
def hello_world(request):
    return HttpResponse("Hello, World!")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  
]
