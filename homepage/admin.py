from django.contrib import admin
from .models import company, user, socialmedia
from .form import CompanyForm
# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    form = CompanyForm
    list_display = ['name','website', 'logo']


class UserAdmin(admin.ModelAdmin):
    list_display = ['fullname','job_role', 'slug']


class socialmediaAdmin(admin.ModelAdmin):
    list_display = ['company','platform', 'link']


admin.site.register(company, CompanyAdmin)
admin.site.register(user, UserAdmin)
admin.site.register(socialmedia, socialmediaAdmin)

