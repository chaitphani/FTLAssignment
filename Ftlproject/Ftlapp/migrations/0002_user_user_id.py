# Generated by Django 2.2.3 on 2020-05-05 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ftlapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
