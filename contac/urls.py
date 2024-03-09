from . import views
from django.urls import path
urlpatterns = [
  path("ruta1", views.contacto, name="contacto")
]
