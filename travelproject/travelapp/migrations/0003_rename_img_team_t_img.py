# Generated by Django 4.2.3 on 2023-07-12 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='img',
            new_name='t_img',
        ),
    ]
