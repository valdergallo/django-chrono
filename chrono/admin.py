from django.contrib import admin
from chrono.models import ChronoDateTime


class ChronoDatetimeAdmin(admin.ModelAdmin):
    search_fields = ('chrono_date__date', 'chrono_time__time')
    list_display = ('id', 'chrono_date', 'chrono_time')


admin.register(ChronoDateTime, ChronoDatetimeAdmin)
