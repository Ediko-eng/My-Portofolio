from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ContactForm
from .models import Project, Skill


def home(request):
    context = {
        "skills": Skill.objects.all(),
        "projects": Project.objects.all(),
        "form": ContactForm(),
    }
    return render(request, "core/home.html", context)


def contact(request):
    if request.method != "POST":
        return redirect(reverse("core:home") + "#contact")

    form = ContactForm(request.POST)

    if form.is_valid():
        message = form.save()

        try:
            send_mail(
                subject=f"Portfolio contact from {message.name}",
                message=(
                    f"From: {message.name} <{message.email}>\n\n{message.message}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_RECIPIENT],
                fail_silently=True,
            )
        except Exception:  # pragma: no cover - never block on email errors
            pass

        messages.success(request, "Thanks! Your message has been sent.")
        return redirect(reverse("core:home") + "#contact")

    # Invalid submission: re-render the page with the bound form and errors.
    context = {
        "skills": Skill.objects.all(),
        "projects": Project.objects.all(),
        "form": form,
    }
    return render(request, "core/home.html", context, status=400)
