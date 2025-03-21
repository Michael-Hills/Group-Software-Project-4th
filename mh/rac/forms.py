# forms.py
from django import forms
from base.models import Profile
from django.forms import ModelForm


class ConcernForm(forms.Form):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    # Section: Date and Person Raising Concern
    date = forms.DateField(label='Date', widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    cr_name = forms.CharField(label='Name of Concern Raiser', max_length=50, required=True)
    cr_contact = forms.CharField(label='Contact Details', max_length=100, required=True)
    cr_org = forms.CharField(label='cr_org', max_length=100, required=True)
    cr_team = forms.CharField(max_length=50, label='Is the person already with a team? (Leave blank if not)', required=False)
    cr_risk = forms.CharField(max_length=500, label='Any known risks', widget=forms.Textarea, required=False)

    # Section: About the Person
    person_name = forms.CharField(label='Name / Initials', max_length=100, required=False)
    person_contact = forms.CharField(label='Contact number', max_length=100, required=False)
    gp_surgery = forms.CharField(label='GP Surgery', max_length=100, required=False)
    nhs_number = forms.IntegerField(label='NHS Number', required=False)
    address = forms.CharField(label='Address', max_length=500, widget=forms.Textarea, required=False)
    walk_in = forms.BooleanField(label='Walk in?', required=False)
    email = forms.EmailField(max_length=100, label='Email', required=False)
    dob = forms.DateField(label='dob', widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    is_homeless = forms.BooleanField(label='Is the person homeless', required=False)
    is_alcoholic = forms.BooleanField(label='Is the person an alcoholic', required=False)
    using_drugs = forms.BooleanField(label='Is the person a regular drug user', required=False)
    taking_medication = forms.BooleanField(label='Are they taking any medication', required=False)

    # Section: About the Concern
    concern_description = forms.CharField(max_length=500, label='Description of Concern', widget=forms.Textarea, required=True)

    # Section: Consent
    consent_checkbox = forms.BooleanField(label='I agree to the terms and give my consent.', required=True)

    # Section: Signature and Date
    signature = forms.CharField(label='Signed', max_length=100, required=True)
    signature_date = forms.DateField(label='Date', widget=forms.DateInput(attrs={'type': 'date'}), required=True)


GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]


class EditConcernForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['RACdate','cr_name','cr_contact','cr_org','cr_team','cr_risk','person_name','person_contact','gp_surgery','nhs_number',
                  'address','walk_in','email','dob','gender','is_homeless','is_alcoholic','using_drugs','taking_medication','concern_description','consent_to_share','signature',
                  'signature','signature_date']
        widgets = {'address':forms.Textarea,
                   'cr_risk':forms.Textarea,
                   'dob':forms.DateInput(attrs={'type': 'date'}),
                   'concern_description':forms.Textarea,
                   'RACdate':forms.DateInput(attrs={'type': 'date'}),
                   'signature_date':forms.DateInput(attrs={'type': 'date'}),
                   'gender':forms.RadioSelect(choices=GENDER_CHOICES),
                   }
                   

    