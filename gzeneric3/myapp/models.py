from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return f"{self.name}"

class Chats(models.Model):
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    texts = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now=True)