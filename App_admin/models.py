from django.db import models


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(null=True, blank=True)
    email2 = models.EmailField(null=True, blank=True)
    location = models.CharField(max_length=250, blank=True, null=True)
    location2 = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=250, blank=True, null=True)
    phone2 = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.email

class About(models.Model):
    id = models.AutoField(primary_key=True)
    core_values = models.CharField(max_length=250, blank=True, null=True)
    bio = models.CharField(max_length=250, blank=True, null=True)
    mission = models.CharField(max_length=250, blank=True, null=True)
    vision = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.bio


category_choice = (
    ("Fixed", "Fixed"),
    ("Negotiable", "Negotiable")
)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=30)
    price = models.CharField(max_length=20)
    image = models.FileField()
    category = models.CharField(choices=category_choice, default="Fixed", max_length=20)
    created_at = models.DateTimeField(auto_now_add = True)
    udpated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=30)
    image = models.FileField()
    created_at = models.DateTimeField(auto_now_add = True)
    udpated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

class BlogComment(models.Model):
    id = models.AutoField(primary_key=True)
    blog_id = models.ForeignKey(Blog, on_delete = models.CASCADE)
    comment = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_id.title
