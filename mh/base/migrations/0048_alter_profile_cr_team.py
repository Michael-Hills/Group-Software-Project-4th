# Generated by Django 4.2.11 on 2024-03-10 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0047_alter_profile_racdate_alter_profile_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cr_team',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
