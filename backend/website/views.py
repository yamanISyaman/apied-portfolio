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
        u = User.objects.get(username=username)
        data = json.loads(request.body.decode())

        print(data)

        send_mail(
            f"Portfolio Contact message from {data['name']}",
            f"from: {data['name']}, email: {data['email']}\nMessage: {data['message']}",
            settings.EMAIL_HOST_USER,
            [
                os.environ["EMAIL_ADMIN"],
            ],
        )

        return JsonResponse(
                {
                    "message": "Thanks for contacting with us",
                },
                status=200,
            )

    return render(request, "website/index.html")