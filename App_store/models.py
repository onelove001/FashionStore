from django.db import models



class Messages(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=255, null=True, blank=True)
    message_sub = models.CharField(max_length=40, null=True, blank=True)
    message_text = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.email


class List(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()

    def __str__(self):
        return self.email
