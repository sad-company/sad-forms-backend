from django.urls import path

from .views import form_view, form_view_by_form_id

urlpatterns = [
    path('', form_view),
    path('<str:form_id>', form_view_by_form_id)
]
