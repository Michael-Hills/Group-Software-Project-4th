import django_filters
from .models import Profile
from django.db import models

"""
class ProfileFilter(django_filters.FilterSet):

   
    class Meta:
        model = Profile
        fields = {
            'concern_level': ['exact'],
            'person_name': ['contains'],
        }

    def __init__(self, *args, **kwargs):
       super(ProfileFilter, self).__init__(*args, **kwargs)
       self.filters['person_name__contains'].label="Name"

"""
    
    

        
        
    