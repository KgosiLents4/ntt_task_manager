from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, TeamMember
from .forms import TaskForm, TeamMemberForm
import logging


def index(request):
    scheduled_tasks = Task.objects.filter(status='scheduled')
    tasks_in_progress = Task.objects.filter(status='in_progress')
    completed_tasks = Task.objects.filter(status='completed')
    deleted_tasks = Task.objects.filter(status='deleted')
    team_members = TeamMember.objects.all()

    context = {
        'scheduled_tasks': scheduled_tasks,
        'tasks_in_progress': tasks_in_progress,
        'completed_tasks': completed_tasks,
        'deleted_tasks': deleted_tasks,
        'team_members': team_members,
    }

    return render(request, 'tasks/index.html', context)

logger = logging.getLogger(__name__)

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # Create a task instance but do not save it to the database yet
            new_task = form.save(commit=False)
            # Set the default status if it's not provided by the form
            if not new_task.status:
                new_task.status = 'scheduled'
            new_task.save()  # Now save the task to the database
            logger.info(f"New task created: {new_task.title} with ID {new_task.id} and status {new_task.status}")
            return redirect('index')
        else:
            # Log form errors if the form is not valid
            logger.error(f"Form errors: {form.errors}")
    else:
        form = TaskForm()

    team_members = TeamMember.objects.all()
    context = {
        'form': form,
        'team_members': team_members,
    }
    return render(request, 'tasks/add_task.html', context)

def move_task_to_in_progress(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.status = 'in_progress'
    task.save()
    return redirect('index')


def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.status = 'completed'
    task.save()
    return redirect('index')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.status = 'deleted'
    task.save()
    return redirect('index')

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm(instance=task)
    
    team_members = TeamMember.objects.all()
    context = {
        'form': form,
        'team_members': team_members,
        'task': task,
    }
    return render(request, 'tasks/edit_task.html', context)

def team_members(request):
    members = TeamMember.objects.all()
    return render(request, 'tasks/team_members.html', {'members': members})

def add_team_member(request):
    if request.method == 'POST':
        form = TeamMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team_members')  # Redirect to team members page after adding member
    else:
        form = TeamMemberForm()
    
    context = {
        'form': form,
    }
    return render(request, 'tasks/add_team_member.html', context)

def edit_team_member(request, member_id):
    member = get_object_or_404(TeamMember, id=member_id)
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('team_members')
    else:
        form = TeamMemberForm(instance=member)

    return render(request, 'tasks/edit_team_member.html', {'form': form})


def delete_team_member(request, member_id):
    member = get_object_or_404(TeamMember, id=member_id)
    if request.method == 'POST':
        member.delete()
        return redirect('team_members')
    return render(request, 'tasks/delete_team_member.html', {'member': member})
