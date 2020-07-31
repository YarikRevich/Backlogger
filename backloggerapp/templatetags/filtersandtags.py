from django.template import Library
import random
import os
from backlogger.settings import MEDIA_ROOT
from backloggerapp.services import create_or_update_pdf
from backloggerapp.models import Project

register = Library()

@register.simple_tag()
def x(*args) -> "Random Position X":
    """Returns a random x"""

    x = random.randrange(5,20)
    return f"{x}em"

@register.simple_tag()
def y(*args) -> "Random Prosition Y":
    """Returns a random y"""

    y = random.randrange(-20,20)
    return f"{y}em"

@register.simple_tag()
def random_image(*args) -> "Random Num":
    """Returns a random background image"""

    image = "https://images.unsplash.com/photo-1553289038-6638b1a1802a?ixlib=rb-1.2.1&auto=format&fit=crop&w=1951&q=80"
        
    return image

@register.simple_tag()
def media_path(image: str,*args) -> "Avatar":
    """Returns a path of user's avatar"""
    
    try:
        path = image.split("/")[1]   
        return f"/static/image/{path}"
    except IndexError:
        pass
    
@register.simple_tag(takes_context=True)
def get_pdf(context,pk: int,*args) -> "PDF file":
    """Returns a path to user's pdf file"""

    create_or_update_pdf(context["user"],pk)
    return f"/static/pdf/{context['user']}_{Project.objects.get(pk=pk).name}.pdf"
