from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('code', 'email', 'name', 'is_reader', 'is_writer', 'is_admin')
    list_filter = ('is_reader', 'is_writer', 'is_admin',)
    fieldsets = (
        (None, {'fields': ('code', 'email', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_reader', 'is_writer', 'is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('code', 'email', 'name', 'password1', 'password2')}
         ),
    )
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
