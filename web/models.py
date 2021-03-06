from django.db import models
from colorfield.fields import ColorField



# Create your models here.
class contact(models.Model):
    joined = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    phoneNumber = models.CharField(max_length=12)
    primaryEmail = models.CharField(max_length=128, unique=True)
    secondaryEmail = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class blogPost(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(contact, on_delete=models.PROTECT)
    title = models.CharField(max_length = 100)
    content = models.TextField()
    posted = models.BooleanField(default=False)

class dashboardElement(models.Model):
    name = models.CharField(max_length=32)
    url = models.CharField(max_length=300)
    width = models.SmallIntegerField(default=350)
    height = models.SmallIntegerField(default=350)
    is_link = models.BooleanField(default=False)
    is_embed = models.BooleanField(default=True)

class siteSetting(models.Model):
    site_title = models.CharField(max_length=32, default="Blog")
    info_banner = models.CharField(max_length=32, default=None, blank=True, null=True)
    color = ColorField(default='#FF0000')
    landing_page_text = models.TextField(null=True)

