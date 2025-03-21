import os
import django
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mh.settings')  # Replace 'yourproject' with your project name
django.setup()

from .models import EncryptedProfile  # Replace 'yourapp' with the name of your app

# Create an instance of EncryptedProfile with all fields filled out
profile = EncryptedProfile(
    RACdate=datetime.date.today(),
    walk_in=True,
    dob=datetime.date(1990, 1, 1),
    referredTo='GP',
    likes=['Large Groups', "1o1's"],
    dislikes=['Large Groups'],
    concern_level='Medium',
    cr_name="Encrypted Test CR Name",
    cr_contact="Encrypted Test CR Contact",
    cr_org="Encrypted Test Organization",
    cr_team="Encrypted Test Team",
    cr_risk="Encrypted Low",
    person_name="Encrypted John Doe",
    person_contact="Encrypted 123456789",
    gp_surgery="Encrypted Test Surgery",
    nhs_number="Encrypted 987654321",
    address="Encrypted 123 Test St, Test City",
    email="encryptedjohn.doe@example.com",
    gender="Encrypted M",
    concern_description="Encrypted No immediate concerns.",
    consent_to_share=True,
    signature="Encrypted John Doe",
    signature_date="Encrypted 2023-01-01",
    referredToMore="Encrypted Specialist Service",
    support_needed="Encrypted Counseling",
    support_accessed="Encrypted None",
    initialDecision="Encrypted To be reviewed",
    personal_plan="Encrypted Follow-up in 3 months"
)

# Save the instance to the database
profile.save()

print("EncryptedProfile instance saved to the database.")
