# Generated by Django 4.0.3 on 2023-05-14 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sugang', '0002_alter_accessurl_testurl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultinfo',
            name='serverTime',
        ),
        migrations.RemoveField(
            model_name='resultinfo',
            name='toAccessURL',
        ),
    ]
