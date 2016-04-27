from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class Post(models.Model):
    #  author is linked to a registered user in the "auth_user" table
    author = models.ForeignKey('accounts.User')        # """ AUTH_USER_MODEL ='accounts.User' in settings"""
    title = models.CharField(max_length=200)

    image = models.ImageField(upload_to='images',
            null=True,
            blank=True,
            width_field="width_field",
            height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
