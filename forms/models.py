from __future__ import annotations

from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class Form(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255)
    questions = models.JSONField(null=False)
    form_id = models.CharField(max_length=64, null=False, unique=True)

    @staticmethod
    def get(form_id: str) -> Form | None:
        try:
            form = Form.objects.get(form_id=form_id)
        except ObjectDoesNotExist:
            return None

        return form


class FormAnswer(models.Model):
    form_id = models.ForeignKey(Form, on_delete=models.CASCADE)
    answer = models.JSONField(null=False)
