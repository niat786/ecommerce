# Generated by Django 3.2.3 on 2021-05-22 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=30)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=20)),
                ('body', models.TextField()),
                ('tags', models.CharField(max_length=50)),
                ('keywords', models.CharField(max_length=40)),
                ('images', models.ImageField(blank=True, default='blank.jpg', upload_to='')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
