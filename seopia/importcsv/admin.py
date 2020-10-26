from django.contrib import admin
from .models import KW
# Register your models here.


@admin.register(KW)
class KWfinder(admin.ModelAdmin):
    list_display = ('id', 'PID', 'keyword', 'landing_status', 'landing_type')
