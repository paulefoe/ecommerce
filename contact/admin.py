from django.contrib import admin
from .models import ContactForm


class ContactForAdmin(admin.ModelAdmin):
    class Meta:
        models = ContactForm

admin.site.register(ContactForm, ContactForAdmin)

