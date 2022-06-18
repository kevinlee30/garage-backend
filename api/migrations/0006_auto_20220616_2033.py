# Generated by Django 3.2.10 on 2022-06-16 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_ambassador_displayimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter name of Project', max_length=200)),
                ('desc', models.CharField(help_text='Enter description of Project', max_length=200)),
                ('displayImage', models.ImageField(default=None, upload_to='Project Image/', verbose_name='Project Image')),
            ],
        ),
        migrations.CreateModel(
            name='StartUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter name of StartUp', max_length=200)),
                ('desc', models.CharField(help_text='Enter description of StartUp', max_length=200)),
                ('displayImage', models.ImageField(default=None, upload_to='StartUp Image/', verbose_name='StartUp Image')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='displayImage',
            field=models.ImageField(default=None, upload_to='Event Image/', verbose_name='Event Image'),
        ),
        migrations.AddField(
            model_name='workshop',
            name='displayImage',
            field=models.ImageField(default=None, upload_to='Workshop Image/', verbose_name='Workshop Image'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='desc',
            field=models.CharField(help_text='Enter description of Workshop', max_length=200),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='name',
            field=models.CharField(help_text='Enter name of Workshop', max_length=200),
        ),
    ]
