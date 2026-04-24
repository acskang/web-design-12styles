from django.urls import path

from . import views

app_name = "showroom"

urlpatterns = [
    path("", views.home, name="home"),
    path("styles/<slug:slug>/", views.detail, name="detail"),
]
