# Generated by Django 3.0.3 on 2020-05-26 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('run', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupmember',
            name='user',
        ),
        migrations.AddField(
            model_name='groupmember',
            name='user_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]