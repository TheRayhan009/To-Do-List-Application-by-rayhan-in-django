# Generated by Django 5.0.7 on 2024-08-19 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datas', '0003_users_c_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='T_task',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
