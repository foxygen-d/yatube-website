# Generated by Django 2.2.16 on 2022-04-28 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20220427_0740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created',
        ),
    ]