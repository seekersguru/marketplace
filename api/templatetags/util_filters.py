from django import template
from datetime import date, timedelta

register = template.Library()
@register.filter(name='get_dictionary_value')
def get_dictionary_value(d,v):
    if d:
        return d.get(v,None)

