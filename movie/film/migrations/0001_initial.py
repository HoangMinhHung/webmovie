# Generated by Django 3.0.3 on 2020-02-24 01:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('director', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0001_initial'),
        ('actor', '0001_initial'),
        ('type', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=255)),
                ('movie_url', models.CharField(max_length=255)),
                ('image_url', models.CharField(max_length=255)),
                ('actor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='actor.Actor')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.Category')),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='director.Director')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='type.Type')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.IntegerField(max_length=1)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='film.Movie')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]