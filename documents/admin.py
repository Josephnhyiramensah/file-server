from django.contrib import admin
from .models import Document

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'uploaded_by', 'downloads', 'emails_sent', 'file')
    search_fields = ('title', 'description')
    list_filter = ('uploaded_by',)

admin.site.register(Document, DocumentAdmin)
