
from django.urls import path
from .import views

urlpatterns = [
    path('first/', views.first,name='f' ),
    path('second/',views.second,name='s'),
    path('third/',views.third,name='t'),
]