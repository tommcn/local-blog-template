from django.contrib import admin
from django.contrib.auth.models import Group

from .models import contact, blogPost, dashboardElement, siteSetting


# Register your models here.

def publish(modeladmin, request, queryset):
    queryset.update(posted=True)
publish.short_description = "Post selected blog post"

def unpublish(modeladmin, request, queryset):
    queryset.update(posted=False)
unpublish.short_description = "Remove selected blog post from blog page"


@admin.register(contact)
class contactAdmin(admin.ModelAdmin):
    search_fields = ['name', 'address', 'phoneNumber', 'primaryEmail']
    list_display = ('name', 'address', 'phoneNumber', 'primaryEmail', 'secondaryEmail')

@admin.register(dashboardElement)
class dashAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'is_link')

@admin.register(blogPost)
class blogAdmin(admin.ModelAdmin):
    search_fields = ['author', 'title', 'content', 'posted']
    list_display = ('author', 'title', 'created', 'posted')
    actions = [publish, unpublish]
    list_filter = ('posted',)

@admin.register(siteSetting)
class settingsAdmin(admin.ModelAdmin):
    search_fields = ['site_title', 'info_banner', 'color']
    list_display = ('site_title', 'info_banner', 'color')
    empty_value_display = "Not Set"


admin.site.unregister(Group)

admin.site.site_header = "Administration Interface"
