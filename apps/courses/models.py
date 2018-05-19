from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) <= 5:
            errors['name'] = "Course name must be longer than five characters."
        if len(postData['description']) <= 15:
            errors['description'] = "Course description must be longer than 15 characters."
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    objects = CourseManager()
