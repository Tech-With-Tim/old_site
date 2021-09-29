from random import randint, shuffle

from allauth.socialaccount.models import SocialAccount
from django import forms
from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator
from django.db.models import Case, F, Sum, When
from django.db.models.aggregates import Avg
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views import View

from TWT.apps.timathon.models.vote import Vote
from TWT.context import get_discord_context
from TWT.discord import client

from ....challenges.models.challenge import Challenge
from ...models.submission import Submission
from ...models.team import Team


class JudgeView(View):
    def get_context(self, request: WSGIRequest) -> dict:
        return get_discord_context(request=request)

    def get(self, request: WSGIRequest):
        context = self.get_context(request=request)
        if not context["is_staff"]:
            messages.add_message(
                request, messages.INFO, "Only staff can access the judging panel."
            )
            return redirect("timathon:Home")

        try:
            challenge = Challenge.objects.get(ended=False, posted=True, type="MO")
        except Challenge.DoesNotExist:
            messages.add_message(
                request, messages.INFO, "There is no ongoing challenge right now."
            )
            return redirect("/")

        submissions = Submission.objects.filter(challenge=challenge).order_by("-votes")
        submissions = list(submissions)

        for submission in submissions:
            members = submission.team.members.all()
            discord_members = []
            for member in members:
                new_member = {}
                try:
                    user = SocialAccount.objects.get(user_id=member.id)
                except SocialAccount.DoesNotExist:
                    pass
                else:
                    new_member["user_id"] = user.uid
                    avatar_url = user.get_avatar_url()
                    if avatar_url.endswith("None.png"):
                        random = randint(0, 4)
                        avatar_url = (
                            f"https://cdn.discordapp.com/embed/avatars/{random}.png"
                        )
                    new_member["avatar_url"] = avatar_url
                    new_member["username"] = user.extra_data["username"]
                    new_member["discriminator"] = user.extra_data["discriminator"]
                    discord_members.append(new_member)
            submission.team.discord_members = discord_members

            submission.judges = [vote.user for vote in submission.votes.all()]
            submission.points = submission.votes.aggregate(
                average=Avg("c1") + Avg("c2") + Avg("c3") + Avg("c4")
            )["average"]

        context["submissions"] = submissions
        context["challenge"] = challenge
        return render(request, "timathon/judge.html", context)
