# Generated by Django 2.1.3 on 2019-03-01 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_job_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='url',
            field=models.CharField(default='I am url', max_length=300),
            preserve_default=False,
        ),
    ]