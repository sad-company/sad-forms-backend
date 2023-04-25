from django import forms


class FormCreateDto(forms.Form):
    name = forms.CharField(max_length=255, required=True)
    description = forms.CharField(max_length=255, required=False)
    questions = forms.JSONField(required=True)
    form_id = forms.CharField(max_length=64, required=True)
