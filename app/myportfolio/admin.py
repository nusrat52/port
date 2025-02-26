from django.contrib import admin

# Register your models here.


from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display=("name", "sirName",)
    prepopulated_fields={"name":('sirName',)}



admin.site.register(User, UserAdmin)

 