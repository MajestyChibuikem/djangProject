from django.urls import path
from . import views

urlpatterns = [
    path('studentss/', views.student_view, name='student_view'),
    path('come_inside', views.come_inside, name='come_inside'),
    path('name', views.say_Name, name='say_Name'),
    path('index/', views.ServerIndex, name='students'),
    path('majesty/', views.majesty, name= 'majesty'),
    path('family/', views.family, name='family'),
    path('aptech/', views.aptech, name='aptech'),
]

