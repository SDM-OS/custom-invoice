from django.contrib import admin
import main.models as models

admin.site.register(models.Job)
admin.site.register(models.Spare)
admin.site.register(models.Attender)
