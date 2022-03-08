from django import template
from contact_form.forms import ContactForm

register = template.Library()


@register.inclusion_tag("contact_form/tags/form.html")
def contact_form():
    return {"contact_form": ContactForm()}