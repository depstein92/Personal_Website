# Generated by Django 2.1.3 on 2019-02-23 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogsModel',
            new_name='Blog',
        ),
    ]
