# Generated by Django 4.1.6 on 2024-03-18 12:23

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0061_alter_profile_gp_surgery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=django_cryptography.fields.encrypt(models.CharField(max_length=100)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='concern_description',
            field=django_cryptography.fields.encrypt(models.CharField(max_length=500)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=django_cryptography.fields.encrypt(models.EmailField(max_length=100)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=django_cryptography.fields.encrypt(models.CharField(max_length=1)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='referredTo',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, choices=[('Devon MIND', 'Devon MIND'), ('HMHT', 'HMHT'), ('GP', 'GP'), ('Resilient Women', 'Resilient Women'), ('Wellbeing Exeter', 'Wellbeing Exeter'), ('Crisis Team', 'Crisis Team'), ('OHMT', 'OHMT'), ('Other', 'Other')], max_length=100, null=True)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='referredToMore',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=200, null=True)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='signature',
            field=django_cryptography.fields.encrypt(models.CharField(max_length=100)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='signature_date',
            field=django_cryptography.fields.encrypt(models.CharField(max_length=100)),
        ),
    ]
