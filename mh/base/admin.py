from django.contrib import admin

# Register your models here.
from .models import Profile, Workshop, FollowUp, Happiness, EncryptedProfile

admin.site.register(Profile)
admin.site.register(Workshop)
admin.site.register(FollowUp)
admin.site.register(Happiness)
admin.site.register(EncryptedProfile)