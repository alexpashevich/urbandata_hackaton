from django.contrib import admin
import timeschedule_analysis.models

# Register your models here.

admin.site.register(timeschedule_analysis.models.Bin)
admin.site.register(timeschedule_analysis.models.City)
admin.site.register(timeschedule_analysis.models.Sample)