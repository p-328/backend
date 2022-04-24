from . import views
from django.urls import path
urlpatterns = [
        path('api/rightnow', views.index),
        path('api/<str:date>', views.get_date)
]
