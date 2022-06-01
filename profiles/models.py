from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):

    """
    Class for the owner of the invoice
    """
    # on_delete = used to tell Django what to do with model instances that depend on the model instance you delete. (e.g. a ForeignKey relationship)
    # CASCADE = When the referenced object is deleted, also delete the objects that have references to it (when you remove a blog post for instance, you might want to delete comments as well).
    # blank = determines whether the field will be required in forms. If blank=True, the field will not be required to fill.
    # auto_now_add = updates the value with the time and date of creation of record.
    # auto_now = updates the value of field to current time and date every time.

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=26, blank=True)
    company_name = models.CharField(max_length=220)
    company_info = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # avatar =
    # company_logo =

    def __str__(self):
        return f"Profile of the user: {self.user.username}"
