from django import template
from django.conf import settings
from socialregistration.utils import _https

register = template.Library()

@register.inclusion_tag('socialregistration/facebook_js.html')
def facebook_js():
    return {'facebook_api_key' : settings.FACEBOOK_API_KEY, 'is_https' : bool(_https())}

@register.inclusion_tag('socialregistration/facebook_button.html', takes_context=True)
def facebook_button(context):
    if not 'request' in context:
        raise AttributeError, 'Please add the ``django.core.context_processors.request`` context processors to your settings.TEMPLATE_CONTEXT_PROCESSORS set'
    logged_in = context['request'].user.is_authenticated()
    next = context['request'].GET.get('next', None)
    return dict(next=next, request=context['request'], logged_in=logged_in, MEDIA_URL=settings.MEDIA_URL)
