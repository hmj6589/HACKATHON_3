# Generated by Django 4.2.4 on 2023-08-24 19:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WalkBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_title', models.CharField(max_length=20)),
                ('d_title', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
                ('create', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.TextField()),
                ('star', models.BooleanField(default=False)),
                ('people', models.PositiveIntegerField()),
                ('completion', models.BooleanField(default=False)),
                ('now_people', models.PositiveIntegerField()),
                ('member', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='walkuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_title', models.CharField(max_length=20)),
                ('d_title', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
                ('create', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.TextField()),
                ('star', models.BooleanField(default=False)),
                ('people', models.PositiveIntegerField()),
                ('total', models.PositiveIntegerField()),
                ('completion', models.BooleanField(default=False)),
                ('now_people', models.PositiveIntegerField()),
                ('member', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
