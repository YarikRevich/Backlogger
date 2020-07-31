from django import forms
from django.forms import ModelForm,modelform_factory
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import AbstractBaseUser
from .models import UserImage,Entry,Project
from django.core import validators
from django.contrib import messages
from django.core.exceptions import ValidationError


class RegestrationForm(forms.ModelForm):
    """Creates form for the registration"""

    class Meta:
        model = User
        fields = ("username","email","password1","password2")
        widgets = {
            "username":forms.TextInput(attrs={
                "class":"form-control",
                "style":"width:20em",
                }),
            "email":forms.TextInput(attrs={
                "class":"form-control",
                "style":"width:20em",
                "id":"inputEmail3",
                }) 
        }
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
                "class":"form-control",
                "style":"width:20em",
                }))        
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
                "class":"form-control",
                "style":"width:20em",
                }))   


class AuthorizationClassForm(AuthenticationForm):
    """Creates form for the authorization"""

    def __init__(self,request,*args, **kwargs):
        super().__init__(*args, **kwargs)

    

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control",
        "style":"width:300px"
        }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "style":"width:300px"
        }))
        

class UserImageForm(forms.ModelForm):
    """Creates form for the adding user image"""

    class Meta:
        model = UserImage
        fields = ("image",)
        
    def clean_image(self):
        
        data = self.cleaned_data["image"]
        return data
    


    def save(self,request):
        filtered = UserImage.objects.filter(owner=request.user.username)
        whole_list = [x.image for x in filtered]
        if whole_list:
            return None
        try:
            new = UserImage.objects.create(owner=request.user.username,image=self.cleaned_data["image"])
        except:
            return False
        return new 
        


class AddEntryForm(forms.ModelForm):
    """Creates form for the adding entry"""

    class Meta:
        model = Entry
        fields = ("name_of_the_entry","description")
        widgets = {
            "name_of_the_entry":forms.TextInput(attrs={
                "class":"form-control",
                "style":"width:15em",
                }),
            "description":forms.Textarea(attrs={
                "class":"form-control",
                "style":"resize:none;width:25em;height:7em",
                }),
        }
    def clean_name_of_the_entry(self):

        data = self.cleaned_data["name_of_the_entry"]
        return data
    
    def clean_description(self):

        data = self.cleaned_data["description"]
        return data
    


        
    def save(self,request,pk):
        project_name = Project.objects.get(pk=pk)
        new = Entry.objects.create(
            name_of_the_entry=self.cleaned_data["name_of_the_entry"],
            project_of_entry=project_name,
            description=self.cleaned_data["description"]
            )
        return new
    


class AddProjectForm(forms.ModelForm):
    """Creates form for the adding project"""

    class Meta:
        model = Project
        fields = ("name","description","projecttype")
        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control","style":"width:20em"}),
            "description":forms.TextInput(attrs={"class":"form-control","style":"width:20em"}),
            "projecttype":forms.Select(attrs={"class":"form-control","style":"width:20em"})
        }

    def clean_name(self):
        data = self.cleaned_data["name"]
        
        return data
    
    def clean_description(self):
        data = self.cleaned_data["description"]
        
        return data
    
    def clean_projecttype(self):
        data = self.cleaned_data["projecttype"]
        
        return data
    
    
    def save(self,request):
        new = Project.objects.create(
            author = request.user.username,
            name = self.cleaned_data["name"],
            description = self.cleaned_data["description"],
            projecttype = self.cleaned_data["projecttype"],
        )
        return new


class AddPlanForm(forms.ModelForm):
    """Creates form for the adding plan"""

    class Meta:
        model = Project
        fields = ("project_plan",)
        widgets = {
            "project_plan":forms.Textarea(attrs={
                "readonly":"true",
                "class":"form-control",
                "id":"plan_form",
                "style":"resize:none;width:40em;height:25em;top:-25%;bottom:0;right:0;left:0;margin:auto;position:absolute;overflow:auto;white-space:pre-wrap"
                })
        }



    def clean_project_plan(self):
        data = self.cleaned_data["project_plan"]
        
        return data
    
    def save(self,author):
        new  = Project.objects.filter(author=author).update(project_plan=self.cleaned_data["project_plan"])
        return new
