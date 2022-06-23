from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
# Create your models here.

#Google drive backend setup. Refer to https://django-googledrive-storage.readthedocs.io/en/latest/
from gdstorage.storage import GoogleDriveStorage
gd_storage = GoogleDriveStorage()
#All file & image fields will accept the property " storage=gd_storage " & that automatically connects to Google Drive 

class Ambassador(models.Model):
    """Model representing an Ambassador"""
    name = models.CharField(max_length=200, help_text='Enter name of Ambassador')
    desc = models.CharField(max_length=200, help_text='Enter description of Ambassador')
    
    displayImage = models.ImageField(upload_to = 'AmbassadorImage/', storage=gd_storage, max_length=100, verbose_name = "Ambassador Image", default = None)
    # contentImages = 
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class AmbassadorImage(models.Model):
    Ambassador = models.ForeignKey(Ambassador, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', storage=gd_storage)
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=200, help_text='Enter name of Event')
    date = models.DateField()
    desc = models.CharField(max_length=200, help_text='Enter description of Event')
    article = models.TextField(default = None)
    isFlagshipEvent = models.BooleanField(default = False)
    displayImage = models.ImageField(upload_to = 'Event Image/', storage=gd_storage, max_length=100, verbose_name = "Event Image", default = None)
#     contentImages = 
    contentVideo = models.FileField(upload_to='Event Videos/', storage=gd_storage, null=True,
                    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    link = models.URLField(default=None)
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    # def get_absolute_url(self):
    #     """Returns the URL to access a particular instance of the model."""
    #     return reverse('model-detail-view', args=[str(self.id)])

class Workshop(models.Model):
    name = models.CharField(max_length=200, help_text='Enter name of Workshop')
    date = models.DateField()
    desc = models.CharField(max_length=200, help_text='Enter description of Workshop')
    article = models.TextField(default = None)
    #ImageField uses Google Drive backend
    displayImage = models.ImageField(upload_to = 'Workshop Image/', storage=gd_storage, max_length=100, verbose_name = "Workshop Image", default = None)
#     contentImages = 
    #FileField uses Google Drive backend
    contentVideo = models.FileField(upload_to='Workshop Videos/', storage=gd_storage, null=True,
                    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    link = models.URLField(default=None)
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    # def get_absolute_url(self):
    #     """Returns the URL to access a particular instance of the model."""
    #     return reverse('model-detail-view', args=[str(self.id)])

class Project(models.Model):
    name = models.CharField(max_length=200, help_text='Enter name of Project')
    desc = models.CharField(max_length=200, help_text='Enter description of Project')
    article = models.TextField(default = None)
    displayImage = models.ImageField(upload_to = 'Project Image/', storage=gd_storage, max_length=100, verbose_name = "Project Image", default = None)
#     contentImages = 
    contentVideo = models.FileField(upload_to='Project Videos/', storage=gd_storage, null=True,
                    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    link = models.URLField(default=None)
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    # def get_absolute_url(self):
    #     """Returns the URL to access a particular instance of the model."""
    #     return reverse('model-detail-view', args=[str(self.id)])

class StartUp(models.Model):
    name = models.CharField(max_length=200, help_text='Enter name of StartUp')
    desc = models.CharField(max_length=200, help_text='Enter description of StartUp')
    article = models.TextField(default = None)
    displayImage = models.ImageField(upload_to = 'StartUp Image/', storage=gd_storage, max_length=100, verbose_name = "StartUp Image", default = None)
#     contentImages = 
    contentVideo = models.FileField(upload_to='StartUp Videos/', storage=gd_storage, null=True,
                    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    link = models.URLField(default=None)
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    # def get_absolute_url(self):
    #     """Returns the URL to access a particular instance of the model."""
    #     return reverse('model-detail-view', args=[str(self.id)])
