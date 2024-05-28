# Generated by Django 5.0.4 on 2024-05-24 23:21

import cloudinary.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=255)),
                ('document_type', models.CharField(max_length=100)),
                ('document_number', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('status', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EntryModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('times_saved', models.IntegerField()),
                ('document', cloudinary.models.CloudinaryField(max_length=255, verbose_name='documento')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'entrys',
            },
        ),
        migrations.CreateModel(
            name='LibraryModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'library',
            },
        ),
        migrations.CreateModel(
            name='LibraryDetailModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status_saved', models.BooleanField(default=True)),
                ('entry_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrys_save.entrymodel')),
                ('library_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libraryDetails', to='entrys_save.librarymodel')),
            ],
            options={
                'db_table': 'library_details',
            },
        ),
    ]
