from django.urls import path
from .views import student_views, search_student,add_student # Past before the urlpatterns variable

urlpatterns = [
    path('student_list', student_views, name = "student_views"), #paste in the urlpatterns as part of the urls
    path('student', search_student, name = 'search_student_name'),
    path('add_student', add_student, name = 'add_student_name'),
]
