from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_task, name='add_task'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('move-to-in-progress/<int:task_id>/', views.move_task_to_in_progress, name='move_task_to_in_progress'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('team/', views.team_members, name='team_members'),
    path('team/add/', views.add_team_member, name='add_team_member'),
    path('team/delete/<int:member_id>/', views.delete_team_member, name='delete_team_member'),
    path('team/edit/<int:member_id>/', views.edit_team_member, name='edit_team_member'),
]
