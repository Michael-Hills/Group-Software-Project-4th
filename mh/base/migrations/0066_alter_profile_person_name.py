# Generated by Django 4.1.6 on 2024-03-18 18:39

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0065_alter_profile_racdate_alter_profile_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='person_name',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=100, null=True)),
        ),
    ]
