from django.contrib import admin
from .models import Poll, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date')

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'poll', 'votes')
