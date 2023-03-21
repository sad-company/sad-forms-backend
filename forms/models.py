from django.db import models


class Form(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255)
    questions = models.JSONField(null=False)
    form_id = models.CharField(max_length=64, null=False, unique=True)


class FormAnswer(models.Model):
    form_id = models.ForeignKey(Form, on_delete=models.CASCADE)
    answer = models.JSONField(null=False)
