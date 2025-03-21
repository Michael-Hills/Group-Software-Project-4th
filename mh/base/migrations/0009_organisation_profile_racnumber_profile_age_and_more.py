# Generated by Django 5.0 on 2023-12-08 15:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_remove_workshop_date_alter_workshop_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='RACNumber',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='consent_to_share',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='initialDecision',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_open',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='support_accessed',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='support_needed',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='walk_in',
            field=models.BooleanField(null=True),
        ),
        migrations.CreateModel(
            name='FollowUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('comments', models.TextField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='referredTo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.organisation'),
        ),
    ]
