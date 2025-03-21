# Generated by Django 4.2.11 on 2024-03-07 23:41

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0042_alter_profile_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='dislikes',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Large Groups', 'Large Groups'), ("1o1's", "1o1's")], max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='likes',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Large Groups', 'Large Groups'), ("1o1's", "1o1's")], max_length=200),
        ),
    ]
