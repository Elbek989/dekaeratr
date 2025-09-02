from django.contrib.auth import get_user_model
from django.db import models


from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Actor(models.Model):
    name=models.CharField(max_length=150)
    birthdate=models.DateField()

    def __str__(self):
        return self.name
User=get_user_model()
class Movie(models.Model):
    name=models.CharField(max_length=150)
    year=models.IntegerField()
    photo=models.ImageField(upload_to='photos/%Y/%m/%d', null=True,blank=True)
    genre=models.CharField(max_length=50)
    actor=models.ManyToManyField(Actor)

    def __str__(self):
        return self.name

class CommitMovie(models.Model):
    title=models.TextField()
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Create your models here.
