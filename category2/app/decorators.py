from django.core.exceptions import PermissionDenied
from simple_decorators.apps.models import Category


def user_is_entry_author(function):
    def wrap(request, *args, **kwargs):
        entry = Category.objects.get(pk=kwargs['id'])
        if entry.created_by == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
