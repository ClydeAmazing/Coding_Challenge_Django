from django.contrib import admin
from . import models

class detailsAdmin(admin.ModelAdmin):
    list_display = ('user', 'marital_status', 'years_of_experience', 'date_of_birth', 'mobile_number')

class educationAdmin(admin.ModelAdmin):
    list_display = ('user', 'degree', 'university', 'gpa')

class attachmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'attachment_file')

admin.site.register(models.applicant_details, detailsAdmin)
admin.site.register(models.applicant_education, educationAdmin)
admin.site.register(models.application_attachment, attachmentAdmin)

