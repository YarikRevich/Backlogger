from django.urls import path,include
from backloggerapp.views import AuthClass,HomeClass,RegClass,LogoutUserClass,delete_avatar,ProjectClass,delete_entry,AddUserImageClass,AddProjectClass,delete_project,AddEntryClass,AddPlanClass
from django.views.decorators.csrf import csrf_exempt
from backloggerapp.decorators import check_recaptcha

"""These are the urls of backlogger application"""


urlpatterns = [
    path("",check_recaptcha(AuthClass.as_view()),name="Authorization"),    #
    path("captcha/",include("captcha.urls")),                               #Authorization,Regestration,Logout paths 
    path("regestration/",RegClass.as_view(),name="Regestration"),           #
    path("homepage/logout",LogoutUserClass.as_view(),name="LogoutUser"),    #

    path("homepage/project",AddProjectClass.as_view(),name="AddProject"),                               #
    path("homepage/image",AddUserImageClass.as_view(),name="AddImage"),                                 #Paths for adding Project,UserImage,Project-plan,Project-entry
    path("homepage/project/add_plan/project_id=<int:pk>",AddPlanClass.as_view(),name="AddPlan"),        #
    path("homepage/project/add_entry/project_id=<int:pk>",AddEntryClass.as_view(),name="AddEntry"),     #

    path("homepage/project/project_id=<int:pk>,page=<int:page>",ProjectClass.as_view(),name="Project"), #Paths for showing Project and Home pages
    path("homepage/",csrf_exempt(HomeClass.as_view()),name="Home"),                                     #

    path("homepage/<int:pk>",delete_avatar),                                                                                                           #
    path("homepage/page/project_id=<int:project_id>/page_to_return=<int:page_to_return>/page_to_delete=<int:pk>",delete_entry,name="DeleteEntry"),     #Paths for deleting UserImage,Project-entry,Project
    path("homepage/project/delete/pk=<int:pk>",delete_project,name="DeleteProject"),                                                                   #
]
