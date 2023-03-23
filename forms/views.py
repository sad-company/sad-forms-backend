from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from django.http import HttpRequest, HttpResponse, HttpResponseNotAllowed, JsonResponse, HttpResponseNotFound

from forms.models import Form


def form_view(request: HttpRequest) -> HttpResponse:
    if request.method != "GET":
        return HttpResponseNotAllowed("GET")

    forms_query_set = Form.objects.all()
    forms_json = list(forms_query_set.values())

    return JsonResponse(forms_json, safe=False)


def form_view_by_form_id(request: HttpRequest, form_id: str) -> HttpResponse:
    if request.method == "GET":
        try:
            form = Form.objects.get(form_id=form_id)
        except ObjectDoesNotExist:
            return HttpResponseNotFound()
        form_json = model_to_dict(form)
        return JsonResponse(form_json)

    if request.method == "DELETE":
        try:
            form = Form.objects.get(form_id=form_id)
        except ObjectDoesNotExist:
            return HttpResponseNotFound()
        form.delete()
        return HttpResponse()

    return HttpResponseNotAllowed("GET", "DELETE")
