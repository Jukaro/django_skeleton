from django import template
import base64
import json

register = template.Library()

@register.filter
def jsonbase64(value):
    encoded = base64.b64encode(json.dumps(value).encode("utf-8")).decode()
    return encoded
