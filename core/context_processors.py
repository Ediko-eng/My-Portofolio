from django.conf import settings

from .models import Profile


def site(request):
    """Expose the profile and public site URL to every template."""
    return {
        "profile": Profile.load(),
        "site_url": settings.SITE_URL,
    }
