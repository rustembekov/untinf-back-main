from django.db import models


class Data(models.Model):
    text = models.CharField(max_length=32)


class Test(models.Model):
    topic = models.CharField(max_length=100)
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

    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=100)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    variant_type_choices = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    )

    answer = models.CharField(max_length=100)
    question_type_choices = (
        ('contextual', 'Contextual'),
        ('ordinary', 'Ordinary'),
        ('multiple-response', 'Multiple-Response'),
    )
    variant = models.CharField(max_length=100, choices=variant_type_choices)
    question_type = models.CharField(max_length=100, choices=question_type_choices)

    def __str__(self):
        return self.title
class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text