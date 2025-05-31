from django.contrib import admin
from .models import Browser

@admin.register(Browser)
class BrowserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'residence_type', 'month_income', 'previous_loan', 'marital_status', 'dependency', 'city', 'state')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('residence_type', 'previous_loan', 'marital_status')

    

# Register your models here.
