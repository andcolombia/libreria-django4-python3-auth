# -*- coding: utf-8 -*-
"""api.views.rank."""

from django.conf import settings
from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sessions.models import Session
from django.middleware.csrf import get_token
from django.http import HttpResponse

class HomeView(LoginRequiredMixin, View):

    """HomeView."""

    def index():
       return HttpResponse("Hola Mundo")

    def get(self, request):
        """Get."""
        sessionid = request.COOKIES['sessionid']
        session = Session.objects.get(pk=sessionid)
        session_data = session.get_decoded()
        print("------session_data----",session_data)

        csrf_token = get_token(request)
        csrf_token_html = (
            '<input type="hidden" '
            'name="csrfmiddlewaretoken" value="{}" />').format(csrf_token)

        return render('home/index.html', {
            'request': request,
            'settings': settings,
            'session_data': session_data,
            'csrf_token_html': csrf_token_html,
        }, status=200)
