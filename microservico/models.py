from django.db import models


class User(models.Model): 
    name = models.CharField(max_length=40) 
    
    def __str__(self):

        return self.name

class Message(models.Model): 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) 
    destination_user_id = models.IntegerField()
    message = models.CharField(max_length=2000) 
    created = models.DateTimeField(auto_now_add=True)

class Actions(models.Model):
    like = models.BooleanField(default=False,null=True)
    unlike = models.BooleanField(default=False,null=True)
    message_id = models.ForeignKey(Message,related_name='likes', on_delete=models.CASCADE) 
    
    