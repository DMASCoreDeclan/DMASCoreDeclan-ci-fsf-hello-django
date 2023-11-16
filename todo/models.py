from django.db import models


# Create your models here.

'''
Create Table Item with 2 fields: name and done
'''


class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    '''
    Returns the NAME of the object instead of the Type of object as defined
    in line 590 of
    https://github.com/django/django/blob/main/django/db/models/base.py
    ''' 
    def __str__(self):
        return self.name
