# Generated by Django 4.2.11 on 2024-03-26 23:59

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0073_alter_profile_is_alcoholic_alter_profile_is_homeless_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='person_name',
            field=django_cryptography.fields.encrypt(models.CharField(default='John Doe', max_length=100)),
            preserve_default=False,
        ),
    ]
