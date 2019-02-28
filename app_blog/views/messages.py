from datetime import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query_utils import Q
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.utils.translation import gettext as _

from toc.utils import QueryObjects, Pagination
from ..forms import SendMessageForm, SendMessageToForm
from ..models import Message


class ConversationsView(LoginRequiredMixin, View):
    def get(self, request):
        queryset = Message.objects.filter(
            Q(user_to=request.user.id) |
            Q(user_from=request.user.id)).order_by('-date_sent')
        queryset = Pagination.paginate_model(request, queryset, 10)
        send_message_form = SendMessageForm(initial={'user_from': request.user})

        # recall exclude current user from queryset
        send_message_form.fields["user_to"].queryset = QueryObjects.get_users_excluding(request.user.id)

        return render(request, 'app_blog/conversations.html', locals())

    def post(self, request):
        send_message_form = SendMessageForm(request.POST)
        if send_message_form.is_valid():
            user_from = QueryObjects.get_user(request.user.id)
            user_to = send_message_form.cleaned_data.get('user_to')
            content = send_message_form.cleaned_data.get('content')
            sent_message = Message(user_from=user_from, user_to=user_to, content=content)
            sent_message.save()
            messages.success(request, _('Message has been sent.'))
        return redirect('conversations')


class SingleMessageView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        participant = (QueryObjects.get_object(Message, kwargs.get('message_id')).user_from == request.user) \
                      or (QueryObjects.get_object(Message, kwargs.get('message_id')).user_to == request.user)

        if request.method == "GET":
            if participant:
                return self.get(request, *args, **kwargs)
            else:
                return redirect('blog-home')

    def get(self, request, message_id):
        private_message = QueryObjects.get_object(Message, message_id)
        if request.user.id == private_message.user_to.id:
            private_message.is_read = True
            private_message.date_read = datetime.now()
            private_message.save()
        return render(request, 'app_blog/message_view.html', locals())


class SendMessageView(LoginRequiredMixin, View):
    def get(self, request):
        send_message_form = SendMessageForm(initial={'user_from': request.user})
        send_message_form.fields["user_to"].queryset = QueryObjects.get_users_excluding(request.user.id)
        return render(request, 'app_blog/send_pm.html', locals())

    def post(self, request):
        send_message_form = SendMessageForm(request.POST)
        if send_message_form.is_valid():
            user_from = QueryObjects.get_user(request.user.id)
            user_to = send_message_form.cleaned_data.get('user_to')
            content = send_message_form.cleaned_data.get('content')
            sent_message = Message(user_from=user_from, user_to=user_to, content=content)
            sent_message.save()
            messages.success(request, _('Message has been sent.'))
        return redirect('conversations')


class SendMessageToView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user_to = QueryObjects.get_user(user_id)
        send_message_to_form = SendMessageToForm()
        return render(request, 'app_blog/send_pm_to.html', locals())

    def post(self, request, user_id):
        send_message_to_form = SendMessageToForm(request.POST)
        if send_message_to_form.is_valid():
            user_from = QueryObjects.get_user(request.user.id)
            user_to = QueryObjects.get_user(user_id)
            content = send_message_to_form.cleaned_data.get('content')
            sent_message = Message(user_from=user_from, user_to=user_to, content=content)
            sent_message.save()
            messages.success(request, _('Message has been sent.'))
        return redirect('conversations')
