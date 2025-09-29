from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_view, name='student_view'),
]

