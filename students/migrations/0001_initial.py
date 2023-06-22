# Generated by Django 4.1.7 on 2023-06-21 12:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Enter Student Name', max_length=40, null=True, verbose_name='Student Name')),
                ('phone', models.CharField(blank=True, help_text='Enter Student Phone Number', max_length=15, null=True, unique=True, verbose_name='Student Phone Number')),
                ('added', models.DateTimeField(default=datetime.datetime(2023, 6, 21, 17, 14, 23, 627706))),
                ('active', models.BooleanField(default=True)),
                ('one_id', models.PositiveIntegerField(default=1000, unique=True, verbose_name='One ID')),
                ('add_to_course', models.ManyToManyField(related_name='add_to_course', to='courses.course')),
                ('add_to_group', models.ManyToManyField(related_name='add_to_group', to='courses.groups')),
                ('user', models.ForeignKey(blank=True, help_text='Select User', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'Students',
                'db_table': 'Students',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Davomat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2023, 6, 21, 17, 14, 23, 628914))),
                ('description', models.TextField(default="Sabab ko'rsatilmagan")),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='davomat', to='students.student', to_field='phone')),
            ],
            options={
                'verbose_name': ' Attendance ',
                'verbose_name_plural': ' Attendances ',
            },
        ),
    ]