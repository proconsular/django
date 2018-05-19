from django.db import models
import re
import bcrypt
from datetime import datetime

class UserManager(models.Manager):
    def validateRequest(self, requestData):
        errors = {}
        name_regex = re.compile(r'^[a-zA-Z]')
        if len(requestData['name']) < 3:
            errors['name_length'] = "Name must be three or more characters long."
        if len(requestData['username']) < 3:
            errors['username_length'] = "Username must be three or more characters long."
        if not name_regex.match(requestData['name']):
            errors['first_name_chars'] = "First Name can only contains letters."
        if len(requestData['password']) < 8:
            errors['password_length'] = "Password must be at least 8 characters."
        if requestData['password'] != requestData['confirm_password']:
            errors['password_match'] = "Passwords don't match."
        return errors

class TripManager(models.Manager):
    def validateRequest(self, requestData):
        errors = []
        if len(requestData['destination']) == 0:
            errors.append("Destination cannot be empty.")
        if len(requestData['description']) == 0:
            errors.append("Description cannot be empty.")
        if len(requestData['fromDate']) == 0:
            errors.append("Travel Date From cannot be empty.")
        if len(requestData['toDate']) == 0:
            errors.append("Travel Date To cannot be empty.")
        # if len(requestData['fromDate']) > 0 and len(requestData['toDate']) > 0:
        try:
            fromDate = datetime.strptime(requestData['fromDate'], "%b %d, %Y")
            toDate = datetime.strptime(requestData['toDate'], "%b %d, %Y")
            if fromDate > toDate:
                errors.append("Start Date cannot be after End Date.")
            present = datetime.now()
            if present > fromDate:
                errors.append("Start Date must be in the future.")
        except Exception as e:
            errors.append("Invalid date format.")
        return errors

class User(models.Model):
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    fromDate = models.DateTimeField()
    toDate = models.DateTimeField()
    creator = models.ForeignKey(User, related_name="created_trips")
    joined_users = models.ManyToManyField(User, related_name="joined_trips")
    created_at = models.DateTimeField(auto_now_add=True)
    objects = TripManager()
