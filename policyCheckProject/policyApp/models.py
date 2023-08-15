from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class PolicyModel(models.Model):
  # pass
  # CHOICES = (
  #       ('Sensemaking', 'sensemaking'),
  #       ('Health', 'health'),
  #       ('Education', 'education'),
       
  #   )

  # policy_making_process = models.CharField(max_length=20, choices=CHOICES, default='Sensemaking')
  user_name = models.CharField(max_length=100)
  policy_choice = models.CharField(max_length=100, default="null")
  
  justified_yes = models.BooleanField(default=False)
  justified_no = models.BooleanField(default=False)
  justified_comment = models.TextField()
  justified_file = models.FileField(upload_to='documents/')
  
  redistributive_yes = models.BooleanField(default=False)
  redistributive_no = models.BooleanField(default=False)
  redistributive_comment = models.TextField()
  redistributive_file = models.FileField(upload_to='documents/')
  
  
  practical_yes = models.BooleanField(default=False)
  practical_no = models.BooleanField(default=False)
  practical_comment = models.TextField()
  practical_file = models.FileField(upload_to='documents/')
  
  interventional_yes = models.BooleanField(default=False)
  interventional_no = models.BooleanField(default=False)
  interventional_comment = models.TextField()
  interventional_file = models.FileField(upload_to='documents/')
  
  
  cost_yes = models.BooleanField(default=False)
  cost_no = models.BooleanField(default=False)
  cost_comment = models.TextField()
  cost_file = models.FileField(upload_to='documents/')
  
  
  finance_yes = models.BooleanField(default=False)
  finance_no = models.BooleanField(default=False)
  finance_comment = models.TextField()
  finance_file = models.FileField(upload_to='documents/')
  
  
  def __str__(self):
        return f"{self.user_name} - {self.policy_choice}"
  
  

  
