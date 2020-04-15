from django.urls import path

from . import views

urlpatterns = [
    path('', views.servers, name='servers'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('server/', views.server, name='server'),
    path('<int:id>/', views.info),
]