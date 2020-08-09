from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class company(models.Model):
    name = models.CharField('Company Name' ,  max_length=100)
    website = models.URLField('Company Website' , max_length=100)
    address = models.TextField('Company Address')
    logo = models.FileField(upload_to='logo/')
    color = models.CharField(max_length=7, default='#3F51B5')

    def __str__(self):
        return self.name
    
class user(models.Model):
    company = models.ForeignKey(company , on_delete = models.CASCADE, default=None)
    fullname = models.CharField('Full Name', max_length=100)
    slug = AutoSlugField(populate_from='fullname', unique_with=['fullname'])
    dob = models.DateField('Date of Birth')
    job_role = models.CharField('Job Title', max_length=100)
    email = models.EmailField('Email Address')
    phone_no = models.CharField('Phone Numner', max_length=15)
    profile = models.FileField(upload_to='profile/')

class socialmedia(models.Model):

    socialplatform = (
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('linkedin', 'Linkedin'),
        ('twitter', 'Twitter'),
    )

    company = models.ForeignKey(company , on_delete = models.CASCADE, default=None, related_name='socialmedia')
    platform = models.CharField(choices=socialplatform, max_length=50)
    link = models.URLField()