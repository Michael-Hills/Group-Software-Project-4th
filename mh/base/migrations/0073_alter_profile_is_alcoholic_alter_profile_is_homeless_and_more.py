# Generated by Django 4.1.6 on 2024-03-25 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0072_alter_profile_is_alcoholic_alter_profile_is_homeless_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='is_alcoholic',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_homeless',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='taking_medication',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='using_drugs',
            field=models.BooleanField(default=False),
        ),
    ]
