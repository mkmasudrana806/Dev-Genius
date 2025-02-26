from django.contrib import admin
from app.models import (
    GeneralInfo,
    ContactFormLog,
    Blog,
    Author,
    Service
)

@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):

    list_display = [
        'company_name',
        'location',
        'email',
        'phone',
        'open_hours',
    ]

    # # show to disable add permission
    # def has_add_permission(self, request, obj=None):
    #     return False

    # # show to disable update permission
    # def has_change_permission(self, request, obj=None):
    #     return False

    # # show to disable delete permission
    # def has_delete_permission(self, request, obj=None):
    #     return False

    # show you can set field to disable update
    readonly_fields = [
        'email'
    ]

@admin.register(ContactFormLog)
class ContactFormLogAdmin(admin.ModelAdmin):

    list_display = [
        'email',
        'is_success',
        'is_error',
        'action_time',
    ]

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    # displays selected fields
    list_display = [
        'category',
        'author',
        'title',
        'blog_image',
        'created_at',
    ]

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    # displays selected fields
    list_display = [
        'first_name',
        'last_name',
    ]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = [
        "title",
        "description"
    ]


    search_fields = [
        "title",
        "description"
    ]
