from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from TWT.context import get_discord_context
from django.contrib import messages


class WeeklyHome(View):
    def get_context(self, request: WSGIRequest) -> dict:
        return get_discord_context(request=request)

    def get(self, request: WSGIRequest):
        if not request.user.is_authenticated:
            messages.add_message(request, messages.INFO, "You are not logged in!")
            return redirect("/")
        context = self.get_context(request=request)
        if not context["is_verified"]:
            return redirect("/")

        return render(
            request=request, template_name="weekly/index.html", context=context
        )
