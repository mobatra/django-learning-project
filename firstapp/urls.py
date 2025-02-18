from django.urls import path
from . import views

urlpatterns = [
  path('<str:name>/<int:age>/', views.user)
]