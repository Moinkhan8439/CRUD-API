from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.api_overview,name="api_overview"),
    path('student-list/',views.student_list ,name="student_list"),
    path('student-detail/<str:pk>/',views.student_detail ,name="student_detail"),
    path('add-student/',views.add_student ,name="add_student"),
    path('update-student/<str:pk>/',views.update_student ,name="update_student"),
    path('delete-student/<str:pk>/',views.delete_student ,name="delete_student"),
]
