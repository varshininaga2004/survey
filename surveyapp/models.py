from django.db import models

# Create your models here.

class Question(models.Model):
    text = models.TextField(unique=True)

    def __str__(self):
        return self.text
    
class Result(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='results')
    yes_count = models.PositiveIntegerField(default=0)
    no_count = models.PositiveIntegerField(default=0)
    not_interested_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Result for question id: {self.question.id}"