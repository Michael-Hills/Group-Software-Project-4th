# Generated by Django 4.0.2 on 2023-12-13 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_alter_profile_issue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='referredTo',
            field=models.CharField(max_length=500),
        ),
    ]
