from . import views
from django.urls import path
urlpatterns = [
  path("contacto/", views.contacto, name="contacto")
]
