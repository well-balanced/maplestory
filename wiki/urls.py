from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.detail, name='detail'),
    path('write', views.write, name='write'),
    path('<int:id>/edit', views.edit, name='edit'),
]
