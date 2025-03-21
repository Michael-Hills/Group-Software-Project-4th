# Generated by Django 4.1.6 on 2024-03-19 13:13

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0066_alter_profile_person_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='signature',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=100, null=True)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='signature_date',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=100, null=True)),
        ),
    ]
