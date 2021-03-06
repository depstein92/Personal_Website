# Generated by Django 2.1.3 on 2019-03-01 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20190228_0158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=75)),
                ('degree', models.CharField(max_length=150)),
                ('years_attended', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=75)),
                ('position', models.CharField(max_length=30)),
                ('date', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
