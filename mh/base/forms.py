from django.forms import ModelForm
from .models import Profile,Workshop,FollowUp, Happiness, Document
from django import forms
from django.core import validators


class ProfileForm(ModelForm):
    """ Form for creating a profile """
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {'address':forms.Textarea,'dob':forms.DateInput(attrs={'type': 'date'}),
                   'concern_description':forms.Textarea}


class DateTimeInput(forms.DateInput):
    """ Date time input cell """
    input_type = 'datetime-local'

class WorkshopForm(ModelForm):
    """ Form to create a workshop """
    class Meta:
        model = Workshop
        fields = '__all__'
        widgets = {'date': DateTimeInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance and instance.date:
            # Format the date as per datetime-local input format
            self.initial['date'] = instance.date.strftime('%Y-%m-%dT%H:%M')

class FollowupForm(ModelForm):
    """ Form to create a workshop """
    class Meta:
        model = FollowUp
        fields = '__all__'
        exclude = ('profile',)
        widgets = {'date': DateTimeInput()}

class EditWorkshopParticipantsForm(ModelForm):
    """ Function to show a single profile """
    class Meta:
        model = Workshop
        fields = ['participants','date','name']
        widgets = {'date': DateTimeInput()}


class ReferralForm(ModelForm):
    """ Function to show a single profile """
    class Meta:
        model = Profile
        fields = ['referredTo','referredToMore']
        widgets = {'referredToMore':forms.Textarea}

    def clean(self):
        super().clean()
        referred = self.cleaned_data.get('referredTo', False)
        if referred == "Other":
            refType = self.cleaned_data.get('referredToMore', None)
            if not refType:
                
                self.add_error("referredToMore","Please fill in the additional info when selecting 'other")
        return self.cleaned_data
    

class LikesForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['likes','dislikes']
        
class ConcernLevelForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['concern_level']
        widgets = {'concern_level':forms.Select}

class EditHappinessForm(ModelForm):
    class Meta:
        model = Happiness
        fields = ['__all__']
        fields = '__all__'
        exclude = ('profile','workshop')


class PersonalPlanForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['personal_plan']
        widgets = {'personal_plan':forms.Textarea}

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('upload', )
