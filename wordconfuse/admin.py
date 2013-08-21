__author__ = 'intuinno'

from django.contrib import admin
from wordconfuse.models import GameScores,Words

class WordAdmin(admin.ModelAdmin):
    list_display = ['word','definition']

    search_fields = ['word','definition']

admin.site.register(Words, WordAdmin)




