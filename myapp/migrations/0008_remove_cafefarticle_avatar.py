# Generated by Django 3.2.7 on 2021-12-14 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_delete_cafefsource'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cafefarticle',
            name='avatar',
        ),
    ]
