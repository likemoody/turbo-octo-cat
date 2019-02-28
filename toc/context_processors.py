import datetime

from django.db.models.query_utils import Q

from .settings import PROJECT_VERSION
from app_blog.models import Message


def project_general(request):
    ctx = {
        'project_version': PROJECT_VERSION,
        'current_date'   : datetime.datetime.now(),
        'project_name'   : 'Post My Dream',
    }
    return ctx


def unread_messages(request):
    private_messages = Message.objects.filter(
        Q(user_to=request.user.id) |
        Q(user_from=request.user.id))
    unread_pm = len(private_messages.filter(
        is_read=False,
        user_to=request.user.id))
    ctx = {
        'unread_messages': unread_pm,
    }
    return ctx
