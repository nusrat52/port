from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="homePage"),
    path('resume/', views.resume, name="resume"),
    path('contact/', views.contact, name="contact"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('project/<slug>/', views.detailed, name="detailed"),
]
