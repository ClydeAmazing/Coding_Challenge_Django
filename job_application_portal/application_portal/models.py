import uuid
from django.db import models
from django.contrib.auth.models import User

class applicant_details(models.Model):
    MARITAL_STATUS_CHOICES = (
        ('Single', 'Single'),
        ('Married', 'Married')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES)
    dependents = models.IntegerField(verbose_name='No. of Dependents', null=True, blank=True)
    years_of_experience = models.IntegerField(null=True, blank=True)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    country = models.CharField(verbose_name='Country of Residence', max_length=100)
    city = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Applicant Details'
        verbose_name_plural = 'Applicant Details'


class applicant_education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    degree = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    gpa = models.FloatField(verbose_name='GPA')

    class Meta:
        verbose_name = 'Applicant Education'
        verbose_name_plural = 'Applicant Education'

# Upload path directory or user file attachments
# file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
def user_attachment_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class application_attachment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # description = models.CharField(max_length=255, null=True, blank=True)
    attachment_file = models.FileField(verbose_name='File', upload_to=user_attachment_path, null=True, blank=True)

    class Meta:
        verbose_name = 'Application Attachments'
        verbose_name_plural = 'Application Attachments'


