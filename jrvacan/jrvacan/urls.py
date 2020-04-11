"""jrvacan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

# from .web import views
from web.views import MainPageView, SpecialtyVacanciesView, CompanyView, VacancyView, VacanciesView

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('vacancies/', VacanciesView.as_view(), name='vacancies'),
    path('jobs/cat/<str:code>/', SpecialtyVacanciesView.as_view(), name='sp_vacancies'),
    path('companies/<int:pk>/', CompanyView.as_view(), name='company'),
    path('jobs/<int:pk>/', VacancyView.as_view(), name='vacancy'),

    path('admin/', admin.site.urls),
]