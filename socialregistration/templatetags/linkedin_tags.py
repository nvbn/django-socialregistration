"""
Created on 22.09.2009

@author: alen
"""
from django import template
from django.conf import settings

register = template.Library()

@register.inclusion_tag('socialregistration/linkedin_button.html', takes_context=True)
def linkedin_button(context):
    if not 'request' in context:
        raise AttributeError, 'Please add the ``django.core.context_processors.request`` context processors to your settings.CONTEXT_PROCESSORS set'
    logged_in = context['request'].user.is_authenticated()
    next = context['request'].GET.get('next', None)
    return dict(next=next, request=context['request'], logged_in=logged_in, MEDIA_URL=settings.MEDIA_URL)
