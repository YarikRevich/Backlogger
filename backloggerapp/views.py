from django.urls import reverse_lazy,reverse
from django.template import loader
from django.shortcuts import render,HttpResponse,redirect
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator
from django.views.generic import View,CreateView,FormView,DeleteView,ListView,FormView

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login,logout

from backloggerapp.backends import CustomAuthentication 
from backloggerapp.models import Project,UserImage,Entry
from backloggerapp.forms import UserImageForm,AddEntryForm,AddProjectForm,RegestrationForm,AuthorizationClassForm,AddPlanForm
from backloggerapp.services import delete_project_by_pk,delete_entry_by_pk,get_and_delete_avatar,get_query_to_paginate,get_project_by_autor,get_image_by_owner,create_or_update_pdf,delete_pdf




class AuthClass(TemplateView):
    """Authorize user on website"""

    template_name = "backloggerapp/authorization.html"

    def get(self,request,*args, **kwargs):
                
        if request.user.is_authenticated:
            messages.info(request,"You have already been logined,press the button to go at the next page")
            return self.render_to_response(context={"form":AuthorizationClassForm(request.GET)})
        return self.render_to_response(context={"form":AuthorizationClassForm(request.GET)})
           
    def post(self,request,*args, **kwargs):

        auth = CustomAuthentication()
        authentification = auth.authenticate(email=request.POST["username"],password=request.POST["password"])
        if authentification:
            if request.recaptcha_is_valid:
                login(request,authentification)
                messages.success(request,"You have successfully been logined")
                return redirect("Home")
        messages.error(request,"You have written wrong credentials")
        return super().get(request,*args,**kwargs)


class RegClass(CreateView):
    """Creates form for the registration"""
    
    form_class = RegestrationForm
    template_name = "backloggerapp/regestration.html"
    success_url = reverse_lazy("Authorization")
    def form_valid(self,form) -> "AuthorizationPage":
        form = RegestrationForm(self.request.POST)
        if form.is_valid():
            form.save()
            messages.success(self.request,"You have been registrated")
            return redirect("Authorization")
        messages.error(self.request,"Something went wrong")
        return redirect("Authorization")


class LogoutUserClass(LogoutView):
    """Logouts user from the site"""

    def dispatch(self,request,*args, **kwargs) -> "dispatcher response":
        response = super().dispatch(request,*args,**kwargs)
        messages.success(request,"You have successfully logged out")
        return response
    


    
class HomeClass(LoginRequiredMixin,TemplateView):
    """Shows main homepage and generates two forms: UserImageForm, AddProjectForm"""

    template_name = "backloggerapp/homepage.html"
    success_url = reverse_lazy("Home")

    def get(self,request,*args, **kwargs) -> "HomePage":
        image_form = UserImage()
        project_form = AddProjectForm()
        context = self.get_context_data(**kwargs)
        context["image_form"] = image_form
        context["project_form"] = project_form
        context["user"] = self.request.user.username

        context["avatar"] = get_image_by_owner(self.request.user.username)[1][0]\
                            if get_image_by_owner(self.request.user.username) \
                            else get_image_by_owner(self.request.user.username)

        context["pk"] = get_image_by_owner(self.request.user.username)[0][0]\
                        if get_image_by_owner(self.request.user.username)\
                        else get_image_by_owner(self.request.user.username)
        
        context["projects"] = get_project_by_autor(self.request.user.username)
        context["pdf"] = f"{self.request.user.username}.pdf"

        return self.render_to_response(context=context)
    
class AddUserImageClass(FormView,HomeClass):
    """Form which adds user's profile image a.k.a avatar"""

    form_class = UserImage
    template_name = "backloggerapp/homepage.html"
    

    def post(self,request,*args, **kwargs) -> "HomePage":
        my_form = UserImageForm(self.request.POST,self.request.FILES)
        if my_form.is_valid():
            my_form_save = UserImageForm()
            my_form_save.image = my_form.cleaned_data["image"]
            if my_form.save(self.request) == None:
                messages.error(self.request,"You already have an avatar ")
                return redirect("Home") 
            elif my_form.save(self.request) == False:
                messages.error(self.request,"Check up whether you have not english symbols in the name of your image")
                return redirect("Home")
            messages.success(self.request,"You have set your avatar")
            return redirect("Home")
           


class AddProjectClass(FormView):
    """Form which adds project"""

    form_class = Project

    def post(self,request,*args, **kwargs) -> "HomePage":
        form = AddProjectForm(request.POST)
        if form.is_valid():
            form.save(request)
            messages.success(request,"You have added your project")
            return redirect("Home")
        messages.error(request,"Something went wrong")
        return redirect("Home")
        




class ProjectClass(TemplateView):
    """Shows entries written in the project made by user"""


    template_name = "backloggerapp/projectbacklogs.html"
    
    def get(self,request,*args, **kwargs) -> "ProjectPage":
        add_entry = AddEntryForm()
        add_plan = AddPlanForm(initial={"project_plan":Project.objects.get(author=self.request.user.username).project_plan})

        context = self.get_context_data(**kwargs)

        queryset = get_query_to_paginate(pk=self.kwargs["pk"])
        paginator = Paginator(queryset,4)
        page_num = paginator.get_page(self.kwargs["page"])
        context["entries"] = page_num
        context["pk"] = self.kwargs["pk"] 
        context["form_entry"] = add_entry
        context["form_plan"] = add_plan

        return self.render_to_response(context=context)


        

class AddEntryClass(FormView):
    """Adds entry to the model"""    

    form_class = AddEntryForm

    def post(self,request,*args, **kwargs) -> "ProjectPage":
        form = AddEntryForm(request.POST)
        if form.is_valid():
            form.save(request,self.kwargs["pk"])
            return redirect("Project",pk=self.kwargs["pk"],page=1)
        return redirect("Project",pk=self.kwargs["pk"],page=1)


class AddPlanClass(FormView):
    """Adds plan to the model"""
    
    form_class = AddPlanForm

    def post(self,request,*args, **kwargs) -> "ProjectPage":
        form = AddPlanForm(request.POST)
        if form.is_valid():
            form.save(author=request.user.username)
            return redirect("Project",pk=self.kwargs["pk"],page=1)
        return redirect("Project",pk=self.kwargs["pk"],page=1)

    
    
def delete_avatar(request,pk: int) -> "HomePage":
    """Deletes user's avatar from his profile"""

    get_and_delete_avatar(pk)
    messages.success(request,"You have deleted your avatar")
    return redirect("Home")



def delete_entry(request,pk: int,project_id: int,page_to_return: int) -> "ProjectPage":
    """Deletes user's entry from his project"""

    delete_entry_by_pk(pk)
    return redirect("Project",pk=project_id,page=page_to_return)
    

def delete_project(request,pk: int) -> "HomePage":
    """Deletes user's project and its pdf project-history"""

    delete_pdf(author=request.user.username)
    delete_project_by_pk(pk)
    return redirect("Home")
