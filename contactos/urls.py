from django.urls import path
from contactos import views

urlpatterns = [
    path('contactos/',views.contacto,name='contacts'),
    path('contacto/',views.unContacto,name="contactss")
]