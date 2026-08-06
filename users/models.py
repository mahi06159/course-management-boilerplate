from django.db import models

# Create your models here.

class Tier(models.Model):
  name = models.CharField(max_length=100)
  max_requests = models.IntegerField()
  window_seconds = models.IntegerField()

  def __str__(self):
    return self.tiername

  
class User(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField(max_length=100, unique=True)
  tier = models.ForeignKey(Tier, on_delete=models.CASCADE, null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)


  def __str__(self):
    return self.name
