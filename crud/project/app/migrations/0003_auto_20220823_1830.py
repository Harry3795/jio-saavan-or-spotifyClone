# Generated by Django 2.2.28 on 2022-08-23 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_vendor'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='sign_up',
            new_name='Registration',
        ),
        migrations.DeleteModel(
            name='vendor',
        ),
    ]
