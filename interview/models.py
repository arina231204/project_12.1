from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class QuestionAnswer(models.Model):
    question = models.CharField(max_length=225)
    short_answer = models.CharField(max_length=225)
    answer = models.TextField(blank=True, null=True, default=0)
    importance = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
