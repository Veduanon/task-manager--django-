# models.py

from datetime import timezone
from django.db import models

class Genders(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=10, null=False)

class Countries(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)

class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150, null=False)
    parent_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    fio = models.CharField(max_length=150, null=False)
    birthday = models.DateField(null=True, blank=True)
    gender = models.ForeignKey(Genders, on_delete=models.CASCADE, null=False)
    email = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

class Films(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150, null=False)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE, null=False)
    duration = models.SmallIntegerField(null=False)
    year_of_issue = models.PositiveSmallIntegerField(null=False)
    age = models.PositiveSmallIntegerField(null=False)
    link_img = models.CharField(max_length=255, null=True, blank=True)
    link_kinopoisk = models.CharField(max_length=255, null=True, blank=True)
    link_video = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

class CategoryFilms(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=False)
    film = models.ForeignKey(Films, on_delete=models.CASCADE, null=False)

class Reviews(models.Model):
    id = models.BigAutoField(primary_key=True)
    film = models.ForeignKey(Films, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=False)
    message = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

class Ratings(models.Model):
    id = models.BigAutoField(primary_key=True)
    film = models.ForeignKey(Films, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=False)
    ball = models.PositiveSmallIntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
