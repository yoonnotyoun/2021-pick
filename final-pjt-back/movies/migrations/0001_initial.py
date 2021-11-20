# Generated by Django 3.2.3 on 2021-11-20 17:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('overview', models.TextField(null=True)),
                ('poster_path', models.CharField(max_length=255, null=True)),
                ('vote_average', models.FloatField(null=True)),
                ('release_date', models.DateField(null=True)),
                ('adult', models.BooleanField(null=True)),
                ('runtime', models.IntegerField(null=True)),
                ('actors', models.ManyToManyField(related_name='movies', to='movies.Actor')),
                ('genres', models.ManyToManyField(related_name='movies', to='movies.Genre')),
                ('like_users', models.ManyToManyField(related_name='like_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
