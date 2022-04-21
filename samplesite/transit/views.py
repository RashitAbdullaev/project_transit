from .models import Request
from django.views.generic.base import TemplateView
from django.contrib.auth.models import Group
from django.contrib.auth.models import User




class Request_all(TemplateView):
    template_name = 'transit/request.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = Request.objects.all()
        return context
