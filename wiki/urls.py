from django.urls import path
from .views import WriteView, DetailView, EditView, HistoryView

urlpatterns = [
    path('<int:id>', DetailView.as_view(), name='detail'),
    path('write', WriteView.as_view(), name='write'),
    path('<int:id>/edit', EditView.as_view(), name='edit'),
    path('<int:id>/history', HistoryView.as_view(), name='history'),
]
