from django.contrib import admin
from .models import Tag
from tags.models import TaggedItem

# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['label']
    search_fields = ['label']