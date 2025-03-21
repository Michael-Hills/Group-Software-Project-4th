from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.core.validators import MaxValueValidator, MinValueValidator
from django_cryptography.fields import encrypt

reffer_choices = (
    ('Devon MIND','Devon MIND'),
    ('HMHT','HMHT'),
    ('GP','GP'),
    ('Resilient Women','Resilient Women'),
    ('Wellbeing Exeter','Wellbeing Exeter'),
    ('Crisis Team','Crisis Team'),
    ('OHMT','OHMT'),
    ('Other','Other')
)

like_choices = (
    ('Large Groups','Large Groups'),
    ("1o1's","1o1's"),
)

dislike_choices = (
    ('Large Groups','Large Groups'),
    ("1o1's","1o1's"),
)

concern_levels = (
    ('Low','Low'),
    ('Medium','Medium'),
    ('High','High')
)


class EncryptedProfile(models.Model):
    """Model that stores the encrypted profile database"""
    # Unchanged fields
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    RACdate = models.DateField()
    walk_in = models.BooleanField()
    dob = models.DateField()
    referredTo = models.CharField(max_length=100, choices=reffer_choices, null=True, blank=True)
    likes = MultiSelectField(choices=like_choices, max_choices=5, max_length=200, blank=True)
    dislikes = MultiSelectField(choices=dislike_choices, max_choices=5, max_length=200, blank=True)
    concern_level = models.CharField(max_length=20, null=True, blank=True, choices=concern_levels)

    # Encrypted fields
    cr_name = encrypt(models.CharField(max_length=50))
    cr_contact = encrypt(models.CharField(max_length=100))
    cr_org = encrypt(models.CharField(max_length=100))
    cr_team = encrypt(models.CharField(max_length=50, null=True, blank=True))
    cr_risk = encrypt(models.CharField(max_length=500))

    person_name = encrypt(models.CharField(max_length=100))
    person_contact = encrypt(models.CharField(max_length=100))
    gp_surgery = encrypt(models.CharField(max_length=100))
    nhs_number = models.CharField(max_length=100)  # Changed to CharField for encryption
    address = encrypt(models.CharField(max_length=100))
    email = encrypt(models.EmailField(max_length=100))
    gender = encrypt(models.CharField(max_length=1))
    concern_description = encrypt(models.CharField(max_length=500))

    consent_to_share = encrypt(models.BooleanField())
    signature = encrypt(models.CharField(max_length=100))
    signature_date = encrypt(models.CharField(max_length=100))

    referredToMore = encrypt(models.CharField(max_length=200, null=True, blank=True))
    support_needed = encrypt(models.CharField(max_length=500, null=True, blank=True))
    support_accessed = encrypt(models.CharField(max_length=500, null=True, blank=True))
    initialDecision = encrypt(models.CharField(max_length=500, null=True, blank=True))
    personal_plan = encrypt(models.CharField(max_length=500, null=True, blank=True))

    def __str__(self):
        return f"Encrypted Profile ID: {self.id}"

class Profile(models.Model):
    """Model that stores the profile database"""
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    RACdate = models.DateField(null=True,blank=True)
    cr_name = encrypt(models.CharField(max_length=50,null=True,blank=True))
    cr_contact = encrypt(models.CharField(max_length=100,null=True,blank=True))
    cr_org = encrypt(models.CharField(max_length=100,null=True,blank=True))
    cr_team = encrypt(models.CharField(max_length=50,null=True,blank=True))
    cr_risk = encrypt(models.CharField(max_length=500,null=True,blank=True))

    # TODO person_name can't be encrypted for some reason
    person_name = encrypt(models.CharField(max_length=100))
    person_contact = encrypt(models.CharField(max_length=100,null=True,blank=True))
    gp_surgery = encrypt(models.CharField(max_length=100,null=True,blank=True))
    nhs_number = encrypt(models.CharField(max_length=100,null=True,blank=True))
    address = encrypt(models.CharField(max_length=100,null=True,blank=True))
    walk_in = models.BooleanField(null=True,blank=True)
    email = encrypt(models.EmailField(max_length=100,null=True,blank=True))
    dob = encrypt(models.CharField(max_length=100, null=True,blank=True))
    gender = encrypt(models.CharField(max_length=1,null=True,blank=True))
    concern_description = encrypt(models.CharField(max_length=500,null=True,blank=True))
    is_homeless = models.BooleanField(default=False)
    is_alcoholic = models.BooleanField(default=False)
    using_drugs = models.BooleanField(default=False)
    taking_medication = models.BooleanField(default=False)
    
    consent_to_share = models.BooleanField()
    signature = encrypt(models.CharField(max_length=100,null=True,blank=True))
    signature_date = encrypt(models.CharField(max_length=100,null=True,blank=True))

    referredTo = encrypt(models.CharField(max_length=100,choices=reffer_choices,null=True,blank=True))
    referredToMore = encrypt(models.CharField(max_length=200,null=True,blank=True))

    support_needed = encrypt(models.CharField(max_length=500, null=True, blank=True))
    support_accessed = encrypt(models.CharField(max_length=500, null=True, blank=True))
    initialDecision = encrypt(models.CharField(max_length=500, null=True, blank=True))

    personal_plan = encrypt(models.CharField(max_length=500, null=True, blank=True))

    likes = MultiSelectField(choices = like_choices,max_choices=5, max_length=200,blank=True)
    dislikes = MultiSelectField(choices = dislike_choices,max_choices=5, max_length=200,blank=True)

    concern_level = models.CharField(max_length=20,null=True,blank=True,choices=concern_levels)


    def __str__(self):
        return self.person_name
    

class FollowUp(models.Model):
    """Model that stores a follow ups"""
    date = models.DateTimeField()
    comments = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)
    
    @property
    def follow(self):
        return True
    

class Workshop(models.Model):
    """Model that stores a workshops"""
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField()
    participants = models.ManyToManyField(Profile)

    def __str__(self):
        return self.name
    
    @property
    def follow(self):
        return False



class Happiness(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop,on_delete=models.CASCADE)
    before = models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(0)],null=True,blank=True)
    after = models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(0)],null=True,blank=True)
    attended = models.BooleanField()

class Document(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(upload_to='documents/')

