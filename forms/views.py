from django.http import HttpRequest, HttpResponse, HttpResponseNotAllowed, JsonResponse

from forms.models import Form


def form_view(request: HttpRequest) -> HttpResponse:
    if request.method != "GET":
        return HttpResponseNotAllowed("GET")

    forms_query_set = Form.objects.all()
    forms_json = list(forms_query_set.values())

    return JsonResponse(forms_json, safe=False)
