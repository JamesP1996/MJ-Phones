from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User

# On Recieving a Post_Save request from a User. Create a Object Instance of That User in the Database
@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        
# Then Save the Changes 
@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwags):
    instance.profile.save()