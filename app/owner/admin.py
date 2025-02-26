from django.contrib import admin

 
from .models import Owner, Testimonials, Tools, Experience, Education, ProjectImages, Projects, Contact


from django.utils.html import format_html
class OwnerAdmin(admin.ModelAdmin):
    list_display=("name", "sirName",)
    prepopulated_fields={"name":('sirName',)}






# class ProjectImageInline(admin.TabularInline):  
#     model = ProjectImages
#     extra = 1   
#     readonly_fields = ["preview"]

    def preview(self, obj):
        """Display image preview in admin"""
        if obj.image:
            return format_html('<img src="{}" style="width:100px; height:auto;">', obj.image.url)
        return ""

class ProjectAdmin(admin.ModelAdmin):
    list_display = ["slug", "date", "description"]
    search_fields = ["slug", "description"]
    prepopulated_fields = {"slug": ("description",)}  # Auto-generate slug
    # inlines = [ProjectImageInline]  








admin.site.register(Owner, OwnerAdmin)
admin.site.register(Testimonials)
admin.site.register(Tools)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(ProjectImages)
admin.site.register(Projects, ProjectAdmin)
admin.site.register(Contact)
 