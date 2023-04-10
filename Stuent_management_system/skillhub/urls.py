from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
  path('',views.index,name='index'),
  path('all_stud',views.all_stud,name='all_stud'),
  path('add_stud',views.add_stud,name='add_stud'),
  path('remove_stud',views.remove_stud,name='remove_stud'),
   path('remove_stud/<int:st_id>',views.remove_stud,name='remove_stud'),
  #path('filter_stud',views.filter_stud,name='filter_stud'),
 

]
