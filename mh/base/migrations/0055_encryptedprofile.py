# Generated by Django 4.1.6 on 2024-03-17 14:03

from django.db import migrations, models
import django_cryptography.fields
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0054_remove_profile_encrypted_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='EncryptedProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('RACdate', models.DateField()),
                ('walk_in', models.BooleanField()),
                ('dob', models.DateField()),
                ('referredTo', models.CharField(blank=True, choices=[('Devon MIND', 'Devon MIND'), ('HMHT', 'HMHT'), ('GP', 'GP'), ('Resilient Women', 'Resilient Women'), ('Wellbeing Exeter', 'Wellbeing Exeter'), ('Crisis Team', 'Crisis Team'), ('OHMT', 'OHMT'), ('Other', 'Other')], max_length=100, null=True)),
                ('likes', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Large Groups', 'Large Groups'), ("1o1's", "1o1's")], max_length=200)),
                ('dislikes', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Large Groups', 'Large Groups'), ("1o1's", "1o1's")], max_length=200)),
                ('concern_level', models.CharField(blank=True, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], max_length=20, null=True)),
                ('cr_name', django_cryptography.fields.encrypt(models.CharField(max_length=50))),
                ('cr_contact', django_cryptography.fields.encrypt(models.CharField(max_length=100))),
                ('cr_org', django_cryptography.fields.encrypt(models.CharField(max_length=100))),
                ('cr_team', django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=50, null=True))),
                ('cr_risk', django_cryptography.fields.encrypt(models.CharField(max_length=500))),
                ('person_name', django_cryptography.fields.encrypt(models.CharField(max_length=100))),
                ('person_contact', django_cryptography.fields.encrypt(models.CharField(max_length=100))),
                ('gp_surgery', django_cryptography.fields.encrypt(models.CharField(max_length=100))),
                ('nhs_number', django_cryptography.fields.encrypt(models.CharField(max_length=100))),
                ('address', django_cryptography.fields.encrypt(models.CharField(max_length=100))),
                ('email', django_cryptography.fields.encrypt(models.EmailField(max_length=100))),
                ('gender', django_cryptography.fields.encrypt(models.CharField(max_length=1))),
                ('concern_description', django_cryptography.fields.encrypt(models.CharField(max_length=500))),
                ('consent_to_share', django_cryptography.fields.encrypt(models.BooleanField())),
                ('signature', django_cryptography.fields.encrypt(models.CharField(max_length=100))),
                ('signature_date', django_cryptography.fields.encrypt(models.CharField(max_length=100))),
                ('referredToMore', django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=200, null=True))),
                ('support_needed', django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=500, null=True))),
                ('support_accessed', django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=500, null=True))),
                ('initialDecision', django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=500, null=True))),
                ('personal_plan', django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=500, null=True))),
            ],
        ),
    ]
