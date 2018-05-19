from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def validateRequest(self, requestData):
        errors = {}
        name_regex = re.compile(r'^[a-zA-Z]')
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(requestData['first_name']) < 2:
            errors['first_name_length'] = "First Name must be two or more characters long."
        if len(requestData['last_name']) < 2:
            errors['last_name_length'] = "Last Name must be two or more characters long."
        if not name_regex.match(requestData['first_name']):
            errors['first_name_chars'] = "First Name can only contains letters."
        if not name_regex.match(requestData['last_name']):
            errors['last_name_chars'] = "Last Name can only contains letters."
        if len(requestData['password']) < 8:
            errors['password_length'] = "Password must be longer than 8 characters."
        if requestData['password'] != requestData['confirm_password']:
            errors['password_match'] = "Passwords don't match."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
