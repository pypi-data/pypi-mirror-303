import logging

from django import template
from django.conf import settings
from django.utils import translation
from django.utils.safestring import mark_safe

from snart.models import Constant

register = template.Library()

logger = logging.getLogger("templatetags.snart")


@register.simple_tag(takes_context=False)
def snart(key, *args, **kwargs):
    """ """
    # lang = translation.get_language()
    try:
        constant = Constant.objects.get(key=key)
        result = constant.value
    except Constant.DoesNotExist:
        logger.error(f"no translation for '{key}'")
        if settings.DEBUG:
            result = "NO_TRANSLATION"
        else:
            result = ""

    return mark_safe(result)
