# Generated by Django 4.2.5 on 2023-10-03 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('cast_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('director_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('genre_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('title', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('year_released', models.IntegerField(max_length=4)),
                ('duration', models.IntegerField()),
                ('description', models.TextField()),
                ('cast', models.ManyToManyField(to='movie.cast')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.director')),
                ('genre', models.ManyToManyField(to='movie.genre')),
            ],
        ),
    ]
