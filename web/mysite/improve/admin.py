from django.contrib import admin
from .models import Category, Ticket
# Register your models here.


class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'created_date')
    list_filter = ['user', 'category', 'created_date']
    search_fields = ['title', 'text']


admin.site.register(Ticket, TicketAdmin)
