# Generated by Django 2.1.2 on 2018-11-20 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('closed', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('closed_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
