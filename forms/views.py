from django.http import HttpRequest, HttpResponse, HttpResponseNotAllowed


def form_view(request: HttpRequest) -> HttpResponse:
    if request.method != "GET":
        return HttpResponseNotAllowed("GET")

    raise NotImplementedError()
