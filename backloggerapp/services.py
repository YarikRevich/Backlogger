import os
import backlogger.settings
from .pdf_creator import update_or_create_pdf
from typing import Union
from .models import Project,Entry,UserImage
from fpdf import FPDF
from backlogger.settings import STATICFILES_DIRS,MEDIA_ROOT


def delete_project_by_pk(pk: int) -> None:
    """Deletes project from 'Project' by primary key"""

    project = Project.objects.get(pk=pk)
    project.delete()


def delete_entry_by_pk(pk: int) -> None:
    """Deletes entry from 'Entry' by primary key"""

    entry = Entry.objects.get(pk=pk)
    entry.delete()

def get_and_delete_avatar(pk: int) -> None:
    """Deletes user's avatar from 'UserImage' by primary key"""

    img = UserImage.objects.get(pk=pk) 
    
    def _delete_thumbnail_by_format() -> None:
        """Deletes thumbnail by its format"""
        
        formats = ["jpg","png","jpeg"]
        try:
            os.remove(os.path.join(MEDIA_ROOT,f"{img.image}.50x50_q95_crop-scale.{formats.pop(0)}"))
            return None
        except:
            return _delete_thumbnail_by_format()
        
    os.remove(os.path.join(MEDIA_ROOT,str(img.image)))
    _delete_thumbnail_by_format()
    
    img.delete()

def get_query_to_paginate(pk: int) -> "QuerySet":
    """Returns  queryset from 'Entry' to paginate it after"""

    project_name = Project.objects.get(pk=pk)
    queryset = Entry.objects.filter(project_of_entry=project_name)
    return queryset


def get_project_by_autor(author: str) -> "Project":
    """Returns 'Project' filtered by author name"""

    return Project.objects.filter(author=author)


def get_image_by_owner(owner: str) -> "FilteredUserImage":
    """Returns 'UserImage filtered by its owner'"""

    image = UserImage.objects.filter(owner=owner)
    return ([x.pk for x in image],[x.image for x in image]) if image else False


def create_or_update_pdf(owner: str,pk: int) -> "_update_pdf if exists or _create_pdf if not":
    """Calls update func if pdf file already exists and creates if not"""

    project = Project.objects.filter(pk=pk)
    entries = Entry.objects.filter(project_of_entry=[x.name for x in project][0])
    
    return update_or_create_pdf(owner=owner,project=project,entries=entries)

def delete_pdf(author: str) -> None:
    """Deletes user's pdf project-history"""

    os.remove(os.path.join(MEDIA_ROOT,f"pdf/{author}_{Project.objects.get(author=author)}.pdf"))

