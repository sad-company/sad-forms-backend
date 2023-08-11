import json

from django.db import DatabaseError
from django.forms.models import model_to_dict
from django.http import HttpRequest, HttpResponse, HttpResponseNotAllowed, JsonResponse, HttpResponseNotFound, \
    HttpResponseBadRequest, HttpResponseServerError
from jsonschema import validate
from jsonschema.exceptions import ValidationError

from .dtos import FormCreateDto
from .models import Form


def form_view(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        forms_query_set = Form.objects.all()
        forms_json = list(forms_query_set.values())
        return JsonResponse(forms_json, safe=False)

    if request.method == "POST":
        form_create_dto = FormCreateDto(request.POST)
        if not form_create_dto.is_valid():
            return HttpResponseBadRequest("Form is not valid!")

        try:
            validate(instance=form_create_dto.cleaned_data['questions'], schema=FORM_CREATE_QUESTIONS_JSONSCHEMA)
        except ValidationError as e:
            return HttpResponseBadRequest(f"Questions is not valid! {e}")

        try:
            Form.objects.create(**form_create_dto.cleaned_data)
        except DatabaseError as e:
            return HttpResponseServerError(e)

        return HttpResponse()

    return HttpResponseNotAllowed("GET", "POST")


def form_view_by_form_id(request: HttpRequest, form_id: str) -> HttpResponse:
    if request.method == "GET":
        form = Form.get(form_id)

        if form is None:
            return HttpResponseNotFound()

        form_json = model_to_dict(form)
        return JsonResponse(form_json)

    if request.method == "DELETE":
        form = Form.get(form_id)

        if form is None:
            return HttpResponseNotFound()

        form.delete()
        return HttpResponse()

    return HttpResponseNotAllowed("GET", "DELETE")


def load_form_create_questions_jsonschema():
    with open('forms/json_schemas/form_create_questions.json', 'r') as raw_json_schema:
        return json.load(raw_json_schema)


FORM_CREATE_QUESTIONS_JSONSCHEMA = load_form_create_questions_jsonschema()
