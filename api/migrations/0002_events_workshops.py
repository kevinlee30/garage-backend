# Generated by Django 3.2.10 on 2022-06-14 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter name of Event', max_length=200)),
                ('date', models.DateField()),
                ('desc', models.CharField(help_text='Enter description of Event', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Workshops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter name of Event', max_length=200)),
                ('date', models.DateField()),
                ('desc', models.CharField(help_text='Enter description of Event', max_length=200)),
            ],
        ),
    ]
