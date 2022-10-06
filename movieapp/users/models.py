from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    avatar = models.FileField(upload_to = "account",blank=True)
    location = models.CharField(max_length = 100,null = True)
    
    
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance , created, **kwargs ):
    if created:
        Profile.objects.create(user=instance)
        
        
        
# @receiver(post_save, sender=User)
# def user_profile(sender, instance , **kwargs ):
#         instance.profile.save()
        

    