from django import forms
from .models import Task, TeamMember

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'assigned_to', 'start_date', 'due_date']  # 'status' is managed in the view or init

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        # Set the default status to 'scheduled' for new tasks
        if not self.instance.pk:  # Check if this is a new instance
            self.instance.status = 'scheduled'  # Set the status directly on the model instance

    # Optionally include 'status' as a hidden field if you want it to be part of the form during updates
    status = forms.CharField(widget=forms.HiddenInput(), required=False)

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['name', 'role']
