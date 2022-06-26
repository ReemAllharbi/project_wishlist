from django.db import models
from datetime import datetime
import bcrypt 


class UserManager(models.Manager):
    def basic_validator(self,postData):
        errors ={}
        check_username=User.objects.filter(username=postData['username'])

        if len(postData['name']) < 3:
            errors['first_name']="Name must be at least 3 characters"

        if len(postData['username']) < 3:
            errors['first_name']="Username must be at least 3 characters"  

        elif check_username.exists():
            errors['username']="Username already exists."

        if len(postData['datehired']) == 0:
            errors['datehired']='Date hired must be filed'

        elif postData['datehired'] > str(datetime.today()):
            errors['datehired']='Date hired must be in the past'

        if postData['password']!=postData['confirm_password']:
              errors['password']="Password and confirm pw must be at match"

        elif len(postData['password']) < 8:
              errors['password']="Password must be at least 8 characters"  

        return errors

    def login_validator(self,postData):
        errors_login_validator = {}
        check_username=User.objects.filter(username=postData['username-login'])

        if check_username.exists():
            user = User.objects.get(username=postData['username-login'])
            if bcrypt.checkpw(postData['password-login'].encode(), user.password.encode()) == False:
             errors_login_validator['password-login'] = "Wrong password."
        else:
            errors_login_validator['username-login'] = "Username not exists."
    
        return errors_login_validator

    def basic_validator_item(self,postData):
        errors ={}
        if len(postData['item_add']) < 3:
            errors['item_add']="Item must be at least 3 characters"
        if len(postData['item_add']) == 0:
            errors['item_add']='Item must be filed'
        return errors


class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    datehired = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Wishlist(models.Model):
    item = models.CharField(max_length=255)
    added_by = models.ForeignKey(User, related_name="users", on_delete=models.CASCADE) #one to many 
    user_fav = models.ManyToManyField(User, related_name="fav_item") #many to many 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager() 