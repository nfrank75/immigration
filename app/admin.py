from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'pays', 'sujet')
    search_fields = ('name', 'email', 'phone', 'pays', 'sujet')
    list_filter = ('pays', 'sujet')

admin.site.register(Contact, ContactAdmin)