from django.contrib import admin
from .models import Project,UserImage,Entry,ProjectTypes


class OwnFilters(admin.SimpleListFilter):
    title = "Types"
    parameter_name = "types"

    def lookups(self,request,model_admin):
        self.filtered_elements = []
        for element in ProjectTypes.objects.all():
            self.filtered_elements.append((str(element.types),str(element.types)))
        return self.filtered_elements

    def queryset(self,request,queryset):
        for element in self.filtered_elements:
            if self.value() == element[0]:
                types_name = ProjectTypes.objects.get(types=element[0])
                return types_name.related.all()
        

@admin.register(ProjectTypes)
class ProjectTypesAdmin(admin.ModelAdmin):
    search_fields = ("types",)
    

@admin.register(Project)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ("name","projecttype","time")
    list_filter = (OwnFilters,)
    list_select_related = True
    date_hierarchy = "time"


@admin.register(UserImage)
class UserImageAdmin(admin.ModelAdmin):
    list_display = ("owner","image")
    list_select_related = True


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ("name_of_the_entry","description")
    list_filter = ("time",)

