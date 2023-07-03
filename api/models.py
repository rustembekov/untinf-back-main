from django.db import models

class Data(models.Model):
    text = models.CharField(max_length=32)


class Test(models.Model):
    name = models.CharField(max_length=100)
    type_choices = (
        ('Python', 'Python'),
        ('Excel', 'Excel'),
        ('HTML5', 'HTML5'),
    )
    type = models.CharField(max_length=100, choices=type_choices)
    form_choices = (
        ('theory', 'Theory'),
        ('practice', 'Practice'),
    )
    form = models.CharField(max_length=100, choices=form_choices)

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    variant = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    question_type_choices = (
        ('contextual', 'Contextual'),
        ('ordinary', 'Ordinary'),
        ('multiple-response', 'Multiple-Response'),
    )
    question_type = models.CharField(max_length=100, choices=question_type_choices)
