# Generated by Django 4.0.1 on 2023-11-08 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('time', models.DateTimeField()),
                ('participants', models.ManyToManyField(to='base.Profile')),
            ],
        ),
    ]
