from django.contrib import admin
from .models import Tweets,Profile
from django.contrib.auth.models import Group, User


admin.site.unregister(Group)

class ProfileInline(admin.StackedInline):
	model = Profile
	
class UserAdmin(admin.ModelAdmin):
	model = User
	# Just display username fields on admin page
	fields = ["username"]
	inlines = [ProfileInline]

# Unregister initial User
admin.site.unregister(User)

# Reregister User and Profile
admin.site.register(User, UserAdmin)
admin.site.register(Tweets)
#admin.site.register(Profile)




