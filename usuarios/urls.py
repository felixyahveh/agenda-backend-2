from django.urls import path
from usuarios import views

urlpatterns = [
    path('usuarios/',views.user,name="users"),
    path('usuario/',views.unUsuario,name="users"),
    path('logIn/',views.logIn,name="users")
]