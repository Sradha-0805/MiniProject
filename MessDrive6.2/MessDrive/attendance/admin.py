from django.contrib import admin
from .models import attendance, expense, staff_expense
# Register your models here.
admin.site.register(attendance)
admin.site.register(expense)
admin.site.register(staff_expense)