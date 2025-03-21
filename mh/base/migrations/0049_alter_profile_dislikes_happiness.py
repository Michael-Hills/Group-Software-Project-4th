# Generated by Django 4.2.11 on 2024-03-10 15:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0048_alter_profile_cr_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dislikes',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Large Groups', 'Large Groups'), ("1o1's", "1o1's"), ('The Gays', 'The Gays')], max_length=200),
        ),
        migrations.CreateModel(
            name='Happiness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('before', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('after', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.profile')),
                ('workshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.workshop')),
            ],
        ),
    ]
