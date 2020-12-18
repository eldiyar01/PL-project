# Generated by Django 3.1.4 on 2020-12-17 08:10

import clubs.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=clubs.models.upload_club_img)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='clubs.club')),
            ],
        ),
    ]