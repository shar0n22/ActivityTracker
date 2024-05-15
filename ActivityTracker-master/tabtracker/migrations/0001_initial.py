# Generated by Django 4.0.5 on 2023-08-31 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alarmdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alarmdet', models.CharField(default='', max_length=60000, null=True)),
                ('email', models.EmailField(max_length=85)),
            ],
        ),
        migrations.CreateModel(
            name='trackdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opentabs', models.CharField(default='', max_length=60000, null=True)),
                ('closetabs', models.CharField(default='', max_length=60000, null=True)),
                ('activetime', models.CharField(default='', max_length=60000, null=True)),
                ('email', models.EmailField(max_length=85, unique=True)),
            ],
        ),
    ]
