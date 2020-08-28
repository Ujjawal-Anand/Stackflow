import re

from django.conf import settings


def metadata(request):
    """
    Add some generally useful metadata to the template context
    """
    return {'website_name': settings.WEBSITE_NAME,
            'website_tagline': settings.WEBSITE_TAGLINE,
            'homepage_url': settings.HOMEPAGE_URL
            }
