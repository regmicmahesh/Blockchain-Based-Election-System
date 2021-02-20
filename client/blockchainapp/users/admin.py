from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import User, Voter, Candidate, ElectionManager


admin.site.register(User);

# admin.site.register(User)
admin.site.register(Voter)
admin.site.register(Candidate)
admin.site.register(ElectionManager)