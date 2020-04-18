from django.urls import path

from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('upload/', views.upload_image, name='upload'),
    path('<int:id>/', views.info),
]