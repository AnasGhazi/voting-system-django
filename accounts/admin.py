from django.contrib import admin
from .models import Poll, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # Number of extra choice fields to display

class PollAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)


# from django.contrib import admin
# from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib import admin
# from .models import Poll

# admin.site.register(Poll)
# # Unregister the User model from the default admin
# admin.site.unregister(User)

# # Now register the User model with your custom UserAdmin
# class UserAdmin(BaseUserAdmin):
#     list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined')  # Customize displayed fields

# # Register the UserAdmin class with the User model
# admin.site.register(User, UserAdmin)

