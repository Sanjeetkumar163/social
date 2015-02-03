from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.files.storage import FileSystemStorage

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    age = models.IntegerField()
    

class Friendship(models.Model):
  friend1 = models.ForeignKey(UserProfile, related_name="friend1_username", null=True)
  friend2 = models.ForeignKey(UserProfile, related_name="friend2_username", null=True)

  class Meta:
    unique_together = ('friend1', 'friend2',)


class Viewed(models.Model):
    who = models.ForeignKey(UserProfile, related_name="who_username", null=True)
    whose = models.ForeignKey(UserProfile, related_name="whose_username", null=True)
    datetime = models.DateTimeField(auto_now_add=True)


class OverwriteStorage(FileSystemStorage):
    def _save(self, name, content):
        if self.exists(name):
            self.delete(name)
        return super(OverwriteStorage, self)._save(name, content)

    def get_available_name(self, name):
        return name


def file(instance, filename):
    url = "user_image/%s.JPG" % (instance.username.user.username,)
    return url


class UserInformation(models.Model):
    username = models.OneToOneField(UserProfile, related_name="username")
    gender = models.CharField(max_length=10)
    qulification = models.CharField(max_length=300, null=True)
    mobile = models.IntegerField(max_length=12, null=True)
    zip_code = models.IntegerField(null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    about = models.TextField(null=True)
    marital_status = models.CharField(max_length=20)
    image = models.ImageField("Image", upload_to = file, storage=OverwriteStorage(), blank=True, null=True)
    


admin.site.register(UserProfile)
admin.site.register(UserInformation)


