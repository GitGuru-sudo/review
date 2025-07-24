from django.db import models

class activity(models.Model):
    username = models.CharField(max_length=122)
    password = models.CharField(max_length=122)

    def __str__(self):
        return self.username


class Review(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    drc = models.CharField(max_length=122)

    def __str__(self):
        return self.name
