from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import User

import json
import os


# Create your views here.
def index(request):
    return render(request, "website/index.html")


@csrf_exempt
def contact_view(request, username):
    if request.method == "POST":

        data = json.loads(request.body.decode())

        try:
            u = User.objects.get(username=username)

        except:

            return JsonResponse(
                {
                    "type": "danger",
                    "message": "Bad Request! Refresh the page and try again",
                },
                status=401,
            )

        send_mail(
            f"Portfolio Contact message from {data['name']}",
            f"from: {data['name']}, email: {data['email']}\nMessage: {data['message']}",
            settings.EMAIL_HOST_USER,
            [
                u.email,
            ],
        )        

        return JsonResponse(
                {
                    "type": "success",
                    "message": "Thanks for contacting with us",
                },
                status=200,
            )

    return render(request, "website/index.html")