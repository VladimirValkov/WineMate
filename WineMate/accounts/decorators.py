from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

from django.contrib.auth import get_user_model
User = get_user_model()


def reader_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_reader,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def writer_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_writer,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def admin_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_admin,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
