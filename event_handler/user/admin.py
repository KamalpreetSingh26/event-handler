from django.contrib import admin
from .models import Profile,Events,EventMembers,Invites
# Register your models here.
admin.site.register(Profile)
admin.site.register(Events)
admin.site.register(EventMembers)
admin.site.register(Invites)