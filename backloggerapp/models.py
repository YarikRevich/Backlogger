from django.db import models
from django.utils import timezone
from django.core import validators
from django.core.files import File
import os
from io import BytesIO

class ProjectTypes(models.Model):
    
    """
    So,it's a primary model for such one as Project for field 'projecttype'.
    In this one you may write your own types of upcomingly-made projects.
    But it's available only for admins 
    
    """

    types = models.CharField(max_length=30, unique=True, verbose_name="The types of the projects")

    def __str__(self):
        return self.types
    
    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"



class Project(models.Model):

    """
    This model was made for the adding of users' projects.Here you can use
    such fields as:
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    autor = the name of the user who made this project
    name = the name of the future project(primary field of model 'Entry')
    descroptions = the desc of this one
    projecttype = the type of the project(secondary field of model 'ProjectType')
    time = a time when it was made

    """

    author = models.CharField(max_length=200, verbose_name="The author of the entry")
    name = models.CharField(max_length=200, verbose_name="Name of the project", default="-", unique=True, null=True)
    description = models.CharField(max_length=400, verbose_name="Description of the projects", default="-")
    project_plan = models.TextField(max_length=1000, verbose_name="Plan of the project")
    projecttype = models.ForeignKey(ProjectTypes, on_delete=models.CASCADE, related_name="related")
    time = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name="Making time")

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = "Projects"
        verbose_name = "Project"
        ordering = ["-time"]

class Entry(models.Model):

    """
    This model realizes such functianality as the adding of the users' entries
    for different projects.For that you can use such fields:
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    name_of_the_entry = the name of your upcoming entry
    project_of_entry = the name of the entry(secondary field for field 'name' in model 'Project')
    description = the desc of the user's entry
    time = the time of the adding

    """

    name_of_the_entry = models.CharField(max_length=200, unique=True, null=True, default="-")
    project_of_entry = models.ForeignKey(Project, on_delete=models.CASCADE, to_field="name", related_name="+")
    description = models.TextField(max_length=400, verbose_name="Description", default="-")
    time = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name="Making time")
    

    def __str__(self):
        return self.name_of_the_entry
    
    

    class Meta:
        verbose_name_plural = "Entries"
        verbose_name = "Entry"
        ordering = ["-time"]



class UserImage(models.Model):

    """
    This model is used for the adding of the users' avatars
    for that thing you can you these two fields:
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    owner = is used for the adding of the user's  username like id
    image = is userd for the direct adding of the user's avatar

    """
    owner = models.CharField(max_length=20, verbose_name="Owner", default="-")
    image = models.ImageField(upload_to="user_image/",verbose_name="Image")
    

    def __str__(self):
        return self.owner

    class Meta:
        verbose_name_plural = "UserImages"
        verbose_name = "UserImage"
        
