from django.db import models
from django.contrib.auth.models import User

# we will now define signals so our Profile model will be automatically created/updated when we create/update User instances
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    USER_GENDER = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]

    CHAIRPERSON         = 'Chairperson'
    VICE_CHAIRPERSON    = 'Vice Chairperson'
    SECRETARY           = 'Secretary'
    VICESECRETARY       = 'Vice Secretary'
    ITDIRECTOR          = 'IT Director'

    USER_POSITION = [
        (CHAIRPERSON, 'Chairperson'),
        (VICE_CHAIRPERSON, 'Vice Chairperson'),
        (SECRETARY, 'Secretary'),
        (VICESECRETARY, 'Vice Secretary'),
        (ITDIRECTOR, 'IT Director')
    ]
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    gender      = models.CharField(max_length=2, choices=USER_GENDER, default=MALE)
    position    = models.CharField(max_length=225, choices=USER_POSITION, blank=True)
    date        = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()        