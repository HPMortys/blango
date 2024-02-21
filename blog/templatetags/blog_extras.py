from django.contrib.auth.models import User
from django.template import Library
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe

register = Library()


@register.filter(name="author_details")
def author_details(author, request_user=None):
  if not isinstance(author, User) and isinstance(request_user, User):
    return ""

  if author == request_user:
    return format_html('<strong> me </strong>') 
  
  if author.first_name and author.last_name:
    name = escape(f"{author.first_name} {author.last_name}")
  else:
    name = escape(f"{author.username}")
  
  if author.email:
    email = escape(author.email)
    prefix  =f'<a href="mailto":{email}>'
    suffix = "</a>"
  else:
    prefix = ""
    suffix = ""

  return mark_safe(f"{prefix}{name}{suffix}")
  # return format_html('{}{}{}', prefix, name, suffix)
