from django.urls import path
from .views import Write, Detail, Edit

urlpatterns = [
    path('<int:id>', Detail.as_view(), name='detail'),
    path('write', Write.as_view(), name='write'),
    path('<int:id>/edit', Edit.as_view(), name='edit'),
]
