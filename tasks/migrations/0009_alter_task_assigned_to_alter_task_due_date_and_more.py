# Generated by Django 5.0.7 on 2024-07-16 08:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_remove_task_is_deleted_alter_task_assigned_to_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.teammember'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('scheduled', 'Scheduled'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('deleted', 'Deleted')], default='scheduled', max_length=20),
        ),
    ]
