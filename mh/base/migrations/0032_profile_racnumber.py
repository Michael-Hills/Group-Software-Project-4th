# Generated by Django 4.0.1 on 2024-01-18 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0031_remove_profile_racnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='RACNumber',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
