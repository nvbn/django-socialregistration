from django import template
from django.conf import settings
from django.contrib.sites.models import Site
from socialregistration.utils import _https

register = template.Library()

@register.inclusion_tag('socialregistration/hyves_js.html')
def hyves_js():
    return {'hyves_consumer_key' : settings.HYVES_CONSUMER_KEY,
            'site': Site.objects.get_current(),
            'is_https' : bool(_https())}

@register.inclusion_tag('socialregistration/hyves_button.html', takes_context=True)
def hyves_button(context):
    if not 'request' in context:
        raise AttributeError, 'Please add the ``django.core.context_processors.request`` context processors to your settings.CONTEXT_PROCESSORS set'
    logged_in = context['request'].user.is_authenticated()
    next = context['request'].GET.get('next', None)
    return dict(next=next, logged_in=logged_in, request=context['request'], MEDIA_URL=settings.MEDIA_URL)
