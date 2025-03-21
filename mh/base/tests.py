from django.test import TestCase
from .models import Profile,Workshop,FollowUp
import datetime
import warnings
from django.db import connection
from django.utils.crypto import get_random_string
warnings.filterwarnings("ignore")
from django.contrib.auth.models import User
from django.urls import reverse
from .models import EncryptedProfile
import os
import pandas as pd

class ProfileTestCase(TestCase):

    def setUp(self):
        Profile.objects.create(RACdate=datetime.date.today(),cr_name="James",cr_contact = "0771738182",
                               cr_org="University",cr_team="Alcohol",cr_risk="self harm",person_name="James",
                               person_contact="0777173717",gp_surgery="Finchampstead",nhs_number=453534,address="27 Riddle drive",
                               walk_in=True,email="hah@gmail.com",dob=datetime.date.today(),gender="M",concern_description="Alcohol and drug abuse",
                               signature="sdgg",signature_date=datetime.date.today(),consent_to_share=True)
        

        
    def test_profile_created(self):
        """Test to check a profile is created correctly"""
        profile = Profile.objects.get(cr_name="James")
        self.assertEquals(profile.cr_contact, "0771738182")
        
        
    def test_profile_default(self):
        """Test to see the default values are correct"""
        profile = Profile.objects.get(cr_name="James")
        self.assertEquals(profile.referredTo,None)
        

    def test_create_workshop_for_profile(self):
        """Test that a profile can be added to a workshop"""
        profile = Profile.objects.get(id=1)
        workshop = Workshop.objects.create(name="Alcohol workshop",time=datetime.datetime.today())
        self.assertEquals(workshop.participants.count(),0)
        workshop.participants.set([profile])
        self.assertEquals(workshop.participants.count(),1)

    def test_remove_workshop(self):
        """Test that a workshop can be deleted, without deleting the profile"""
        self.assertEquals(len(Profile.objects.all()),1)
        profile = Profile.objects.get(id=1)
        workshop = Workshop.objects.create(name="Alcohol workshop",time=datetime.datetime.today())
        workshop.participants.set([profile])
        self.assertEquals(len(Workshop.objects.all()),1)
        self.assertEquals(workshop.participants.count(),1)
        Workshop.objects.all().delete()
        self.assertEquals(len(Workshop.objects.all()),0)
        self.assertEquals(len(Profile.objects.all()),1)
        self.assertEquals(profile.cr_contact, "0771738182")

    

class WorkshopTestCase(TestCase):
    def setUp(self):
        Profile.objects.create(RACdate=datetime.date.today(),cr_name="James",cr_contact = "0771738182",
                               cr_org="University",cr_team="Alcohol",cr_risk="self harm",person_name="James",
                               person_contact="0777173717",gp_surgery="Finchampstead",nhs_number=453534,address="27 Riddle drive",
                               walk_in=True,email="hah@gmail.com",dob=datetime.date.today(),gender="M",concern_description="Alcohol and drug abuse",
                               signature="sdgg",signature_date=datetime.date.today(),consent_to_share=True)
        
        

    def test_create_workshop(self):
        profile= Profile.objects.get(id=1)
        workshop = Workshop.objects.create(name="Alcohol workshop",time=datetime.datetime.today())
        workshop.participants.set([profile])

        self.assertEquals(workshop.name,"Alcohol workshop")

    def test_remove_participant(self):
        """ Test to see if deleting a profile wont delete a workshop"""
        self.assertEquals(len(Profile.objects.all()),1)

        profile= Profile.objects.get(id=1)
        workshop = Workshop.objects.create(name="Alcohol workshop",time=datetime.datetime.today())
        self.assertEquals(len(Workshop.objects.all()),1)
        workshop.participants.set([profile])
        Profile.objects.all().delete()
        self.assertEquals(len(Profile.objects.all()),0)
        self.assertEquals(len(Workshop.objects.all()),1)

        self.assertEquals(workshop.name,"Alcohol workshop")


class FollowupTestCase(TestCase):

    def setUp(self):
        followupProfile = Profile.objects.create(RACdate=datetime.date.today(),cr_name="James",cr_contact = "0771738182",
                               cr_org="University",cr_team="Alcohol",cr_risk="self harm",person_name="James",
                               person_contact="0777173717",gp_surgery="Finchampstead",nhs_number=453534,address="27 Riddle drive",
                               walk_in=True,email="hah@gmail.com",dob=datetime.date.today(),gender="M",concern_description="Alcohol and drug abuse",
                               signature="sdgg",signature_date=datetime.date.today(),consent_to_share=True)
        

        FollowUp.objects.create(date=datetime.date.today(),comments="Test",profile=followupProfile)

       
    def test_followup_created(self):
        """Test to check a followup can be created, and assign a profile"""
        follow = FollowUp.objects.get(id=1)
        self.assertEquals(follow.comments,"Test")


    def test_followup_deleted(self):
        """ Test a followup can be deleted without deleting a profile"""
        self.assertEquals(len(FollowUp.objects.all()),1)
        FollowUp.objects.all().delete()
        self.assertEquals(len(FollowUp.objects.all()),0)
        profile = Profile.objects.get(id=1)
        self.assertEquals(len(Profile.objects.all()),1)
        self.assertEquals(profile.person_name,"James")

    def test_profile_deleted(self):
        """ Test that if a profile is deleted, the followup is deleted """
        self.assertEquals(len(FollowUp.objects.all()),1)
        Profile.objects.all().delete()
        self.assertEquals(len(FollowUp.objects.all()),0)
        self.assertEquals(len(Profile.objects.all()),0)


class EncryptedProfileTest(TestCase):

    def test_create_encrypted_profile(self):
        # Set up test data
        test_date = datetime.date.today()
        test_datetime = datetime.datetime.now()
        test_dob = datetime.date(1990, 1, 1)
        test_referred_to = 'GP'
        test_likes = ['Large Groups', "1o1's"]
        test_dislikes = ['Large Groups']
        test_concern_level = 'Medium'

        # Create an EncryptedProfile instance
        profile = EncryptedProfile.objects.create(
            RACdate=test_date,
            walk_in=True,
            dob=test_dob,
            referredTo=test_referred_to,
            likes=test_likes,
            dislikes=test_dislikes,
            concern_level=test_concern_level,
            cr_name="Test CR Name",
            cr_contact="Test CR Contact",
            cr_org="Test Organization",
            cr_team="Test Team",
            cr_risk="Low",
            person_name="John Doe",
            person_contact="123456789",
            gp_surgery="Test Surgery",
            nhs_number="987654321",
            address="123 Test St, Test City",
            email="john.doe@example.com",
            gender="M",
            concern_description="No immediate concerns.",
            consent_to_share=True,
            signature="John Doe",
            signature_date="2023-01-01",
            referredToMore="Specialist Service",
            support_needed="Counseling",
            support_accessed="None",
            initialDecision="To be reviewed",
            personal_plan="Follow-up in 3 months"
        )

        # Retrieve the instance from the database
        saved_profile = EncryptedProfile.objects.get(pk=profile.pk)

        # Verify each field
        self.assertEqual(saved_profile.RACdate, test_date)
        self.assertTrue(saved_profile.walk_in)
        self.assertEqual(saved_profile.dob, test_dob)
        self.assertEqual(saved_profile.referredTo, test_referred_to)
        self.assertEqual(list(saved_profile.likes), test_likes)
        self.assertEqual(list(saved_profile.dislikes), test_dislikes)
        self.assertEqual(saved_profile.concern_level, test_concern_level)
        self.assertEqual(saved_profile.cr_name, "Test CR Name")
        self.assertEqual(saved_profile.cr_contact, "Test CR Contact")
        self.assertEqual(saved_profile.cr_org, "Test Organization")
        self.assertEqual(saved_profile.cr_team, "Test Team")
        self.assertEqual(saved_profile.cr_risk, "Low")
        self.assertEqual(saved_profile.person_name, "John Doe")
        self.assertEqual(saved_profile.person_contact, "123456789")
        self.assertEqual(saved_profile.gp_surgery, "Test Surgery")
        self.assertEqual(saved_profile.nhs_number, "987654321")
        self.assertEqual(saved_profile.address, "123 Test St, Test City")
        self.assertEqual(saved_profile.email, "john.doe@example.com")
        self.assertEqual(saved_profile.gender, "M")
        self.assertEqual(saved_profile.concern_description, "No immediate concerns.")
        self.assertTrue(saved_profile.consent_to_share)
        self.assertEqual(saved_profile.signature, "John Doe")
        self.assertEqual(saved_profile.signature_date, "2023-01-01")
        self.assertEqual(saved_profile.referredToMore, "Specialist Service")
        self.assertEqual(saved_profile.support_needed, "Counseling")
        self.assertEqual(saved_profile.support_accessed, "None")
        self.assertEqual(saved_profile.initialDecision, "To be reviewed")
        self.assertEqual(saved_profile.personal_plan, "Follow-up in 3 months")


class EncryptedFieldsTest(TestCase):

    def setUp(self):
        self.profile = EncryptedProfile.objects.create(
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

    def test_encrypted_fields(self):
        encrypted_field_names = [
            'cr_name', 'cr_contact', 'cr_org', 'cr_team', 'cr_risk',
            'person_name', 'person_contact', 'gp_surgery', 'nhs_number',
            'address', 'email', 'gender', 'concern_description',
            'signature', 'signature_date', 'referredToMore',
            'support_needed', 'support_accessed', 'initialDecision', 'personal_plan'
        ]

        # Use Django's connection cursor to execute a raw SQL query to fetch the encrypted fields
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT {', '.join(encrypted_field_names)} FROM {EncryptedProfile._meta.db_table} WHERE id = %s", [self.profile.id])
            encrypted_values = cursor.fetchone()

        # Iterate over the encrypted field values fetched from the database
        for i, encrypted_value in enumerate(encrypted_values):
            self.assertNotEqual(encrypted_value, getattr(self.profile, encrypted_field_names[i]),
                                f"The field '{encrypted_field_names[i]}' is not encrypted properly in the database.")

class ProfileModelTest(TestCase):

    #python manage.py test base.tests.ProfileModelTest
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Profile.objects.create(
            RACdate=datetime.date.today(),
            cr_name='John Doe Encrypted',
            cr_contact='1234567890 Encrypted',
            cr_org='Some Organization Encrypted',
            cr_team='Some Team Encrypted',
            cr_risk='Low Risk Encrypted',
            person_name='Jane Doe Encrypted',
            person_contact='0987654321 Encrypted',
            gp_surgery='Local Surgery Encrypted',
            nhs_number=1234567,
            address='123 Fake Street Encrypted',
            walk_in=True,
            email='janedoe@example.com Encrypted',
            dob=datetime.date.today(),
            gender='F Encrypted',
            concern_description='General Concern Encrypted',
            consent_to_share=True,
            signature='Jane Doe Signature Encrypted',
            signature_date='2024-01-01 Encrypted',
            referredTo='GP Encrypted',
            referredToMore='Additional Referral Info Encrypted',
            support_needed='Support Needed Description Encrypted',
            support_accessed='Support Accessed Description Encrypted',
            initialDecision='Initial Decision Description Encrypted',
            personal_plan='Personal Plan Description Encrypted',
            likes=['Large Groups'],
            dislikes=["1o1's"],
            concern_level='Low'
        )

    def test_profile_creation(self):
        profile = Profile.objects.get(id=1)
        expected_person_name = 'Jane Doe Encrypted'
        self.assertEquals(expected_person_name, profile.person_name)
        self.assertTrue(profile.walk_in)
        self.assertEquals(profile.likes, ['Large Groups'])
        self.assertEquals(profile.dislikes, ["1o1's"])
        self.assertEquals(profile.concern_level, 'Low')

class ProfileModelEncryptionTest(TestCase):

    # python manage.py test base.tests.ProfileModelEncryptionTest

    def setUp(self):
        # Set up a Profile instance with test data
        self.test_data = {
            'RACdate': datetime.date.today(),
            'cr_name': 'Encrypted Name',
            'cr_contact': '1234567890',
            'cr_org': 'Test Organization',
            'cr_team': 'Development Team',
            'cr_risk': 'Low Risk',
            'person_name': 'John Doe',
            'person_contact': '0987654321',
            'gp_surgery': 'Central Clinic',
            'nhs_number': 123456789,
            'address': '123 Main St',
            'walk_in': True,
            'email': 'john.doe@example.com',
            'dob': datetime.date.today(),
            'gender': 'M',
            'concern_description': 'General Concern',
            'consent_to_share': True,
            'signature': 'John Doe',
            'signature_date': '2023-01-01',
            'referredTo': 'Devon MIND',
            'referredToMore': 'Specific department',
            'support_needed': 'Support text',
            'support_accessed': 'Previous supports',
            'initialDecision': 'Initial decision text',
            'personal_plan': 'Personal plan text',
            'likes': ['Large Groups'],
            'dislikes': ["1o1's"],
            'concern_level': 'Medium'
        }
        self.profile = Profile.objects.create(**self.test_data)

    def test_encrypted_fields(self):
        # Use a database cursor to query the encrypted fields directly
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT cr_name, person_contact, gp_surgery, address, email, gender, concern_description, signature, signature_date FROM base_profile WHERE id=%s",
                [self.profile.id])
            row = cursor.fetchone()

        # Check that the fields are actually encrypted in the database, not stored in plaintext
        self.assertNotEqual(row[0], 'Encrypted Name')  # cr_name
        self.assertNotEqual(row[1], 'Encrypted Contact Info')  # person_contact
        self.assertNotEqual(row[2], 'Encrypted Surgery')  # gp_surgery
        self.assertNotEqual(row[3], 'Encrypted Address')  # address
        self.assertNotEqual(row[4], 'encrypted@example.com')  # email
        self.assertNotEqual(row[5], 'M')  # gender
        self.assertNotEqual(row[6], 'Encrypted Concern')  # concern_description
        self.assertNotEqual(row[7], 'Encrypted Signature')  # signature
        self.assertNotEqual(row[8], 'Encrypted Date')  # signature_date

class ProfileDataOutputTest(TestCase):

    # python manage.py test base.tests.ProfileDataOutputTest

    @classmethod
    def setUpTestData(cls):
        # Create test user
        test_user = User.objects.create_user(username='testuser', password='12345')
        test_user.save()

        # Create test profile
        Profile.objects.create(
            RACdate=datetime.date.today(),
            cr_name='John Doe Encrypted',
            cr_contact='1234567890 Encrypted',
            cr_org='Some Organization Encrypted',
            cr_team='Some Team Encrypted',
            cr_risk='Low Risk Encrypted',
            person_name='Jane Doe Encrypted',
            person_contact='0987654321 Encrypted',
            gp_surgery='Local Surgery Encrypted',
            nhs_number=1234567,
            address='123 Fake Street Encrypted',
            walk_in=True,
            email='janedoe@example.com Encrypted',
            dob=datetime.date.today(),
            gender='F Encrypted',
            concern_description='General Concern Encrypted',
            consent_to_share=True,
            signature='Jane Doe Signature Encrypted',
            signature_date='2024-01-01 Encrypted',
            referredTo='GP Encrypted',
            referredToMore='Additional Referral Info Encrypted',
            support_needed='Support Needed Description Encrypted',
            support_accessed='Support Accessed Description Encrypted',
            initialDecision='Initial Decision Description Encrypted',
            personal_plan='Personal Plan Description Encrypted',
            likes=['Large Groups'],
            dislikes=["1o1's"],
            concern_level='Low'
        )

    def test_data_output_csv(self):
        # Log in as test user
        login = self.client.login(username='testuser', password='12345')
        self.assertTrue(login)

        # Request the data_output view
        response = self.client.get(reverse('data-output'))
        self.assertEqual(response.status_code, 200)

        # Verify the CSV file was created and contains expected data
        self.assertTrue(os.path.exists('out.csv'))

        # Read the CSV to verify its contents
        df = pd.read_csv('out.csv')
        self.assertEqual(len(df), Profile.objects.count())  # The number of rows in the CSV should match the number of Profile instances

        self.assertIn('TestName0', df['person_name'].values)


        # Clean up the created file
        os.remove('out.csv')