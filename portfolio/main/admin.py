from django.contrib import admin
from django.db import models
from .models import SendMessage
# Register your models here.


class SendMessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'phone_number', 'message', 'sent_at',)
    search_fields = ('email',)
    list_editable = ('message',)
    list_filter = ('sent_at',)
    ordering = ('pk','sent_at',)

admin.site.register(SendMessage, SendMessageAdmin)