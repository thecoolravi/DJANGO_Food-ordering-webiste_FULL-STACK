# Generated by Django 4.2.5 on 2023-09-27 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactenquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=60)),
                ('phone', models.CharField(max_length=50)),
                ('websiteLink', models.CharField(max_length=70)),
                ('message', models.TextField()),
            ],
        ),
    ]
