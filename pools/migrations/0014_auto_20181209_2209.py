# Generated by Django 2.1.3 on 2018-12-09 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0013_auto_20181209_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='choices',
            field=models.ManyToManyField(blank=True, related_name='questions', to='pools.Choice'),
        ),
    ]