from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('next/', views.next, name='next'),
    path('previous/', views.previous, name='previous'),
    path('Page2/', views.Page2, name='Page2'),
    path('Page3/', views.Page3, name='Page3'),
]