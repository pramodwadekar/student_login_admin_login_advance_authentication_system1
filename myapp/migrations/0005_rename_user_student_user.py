# Generated by Django 4.2.6 on 2023-10-23 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='student_user',
        ),
    ]
