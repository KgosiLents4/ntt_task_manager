# Generated by Django 5.0.7 on 2024-07-14 14:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_remove_task_status_task_due_date_task_start_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('in_progress', 'In Progress'), ('completed', 'Completed'), ('deleted', 'Deleted')], default='in_progress', max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.teammember'),
        ),
    ]