# Generated by Django 2.2.28 on 2022-08-23 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vname', models.CharField(max_length=100)),
                ('vemail', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
