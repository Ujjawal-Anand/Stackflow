import datetime
from django import template

register = template.Library()

@register.filter
def split(value, separator=' '):
    return value.split(separator)


@register.filter('timestamp_to_time')
def convert_timestamp_to_time(timestamp):
    return datetime.date.fromtimestamp(int(timestamp))