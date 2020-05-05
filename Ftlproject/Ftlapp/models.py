from django.db import models

# Create your models here.


class User(models.Model):
    user_id=models.CharField(max_length=120, null=True, blank=True)
    name = models.CharField(max_length=120, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class Activity(models.Model):
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)

    ## relations
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='activity_user',
                                     null=True, blank=True)

    def __str__(self):
        return self.user.name