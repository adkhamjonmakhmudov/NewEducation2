# Generated by Django 4.1.7 on 2023-06-22 20:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        ('students', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='student',
            field=models.ManyToManyField(related_name='classes', to='students.student'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='classuser', to=settings.AUTH_USER_MODEL),
        ),
    ]
