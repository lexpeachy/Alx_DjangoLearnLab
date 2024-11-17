from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.title
from django.contrib.auth.models import abstractuser, BaseUserManager

class CustomUser(AbstractUser):
    date_of_birth =models.Datefield(null=True blank=True)
    profile_photo =models.Imagefield(upload_to ='profile_photo/')

    objects = CustomUserManager()
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, date_of_birth=date_of_birth, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, date_of_birth, password, **extra_fields)
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        permissions = [
            ("can_view", "Can view article"),
            ("can_create", "Can create article"),
            ("can_edit", "Can edit article"),
            ("can_delete", "Can delete article"),
        ]
