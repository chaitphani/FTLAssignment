# Generated by Django 2.2.3 on 2020-05-05 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ftlapp', '0002_user_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]