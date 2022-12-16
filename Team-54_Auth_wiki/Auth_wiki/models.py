from django.db import models
from django.contrib.auth.models import

class User(models.Model):
    uuid = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100) 
    created_at = models.DateField()
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

class AuthentificationCode(models.Model):
    uuid = models.CharField(max_length=100, unique=True)
    created_at = models.DateField()
    description = models.TextField(max_length=1000)
    name = models.CharField(max_length=100)

class Reactions(models.Model):
    ReactionType = models.TextChoices('like' | 'love' | 'dislike')
    uuid = models.CharField(max_length=100, unique=True)
    type = models.CharField(blank=True, choices= ReactionType.choices)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, to_field='uuid')
    auth_code_id =
    created_at = models.DateField()

class Comment(models.Model):
     user_id = models.ForeignKey(User, on_delete=models.CASCADE, to_field='uuid')
     auth_code_id = models.ForeignKey(AuthentificationCode, on_delete=models.CASCADE, to_field='uuid')
     content = models.TextField(max_length=1000)
     created_at = models.DateField()

class CodeSample(models.Model):
    uuid = models.CharField(max_length=100, unique=True)
    code_content = models.TextField(max_length=1000)
    auth_code_id = models.ForeignKey(AuthentificationCode, on_delete=models.CASCADE, to_field='uuid')
    created_at = models.DateField()
    language = models.CharField(max_length=100)