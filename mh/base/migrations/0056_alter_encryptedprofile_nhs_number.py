# Generated by Django 4.1.6 on 2024-03-17 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0055_encryptedprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encryptedprofile',
            name='nhs_number',
            field=models.CharField(max_length=100),
        ),
    ]
