# Generated by Django 2.1.3 on 2018-12-09 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0008_auto_20181209_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
    ]
