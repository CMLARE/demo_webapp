# Generated by Django 2.1.3 on 2018-11-11 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Neural',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(verbose_name='date published')),
                ('lat', models.CharField(max_length=200)),
                ('long', models.CharField(max_length=200)),
                ('rain', models.CharField(max_length=200)),
            ],
        ),
    ]
