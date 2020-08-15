from django.urls import path
from wiki.views import test, testt

urlpatterns = [
    path('', test, ),
    path('<int:id>/', testt),
]
