from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls.base import reverse_lazy

from ..forms import UserRegistrationForm

from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.views.generic.edit import FormView, DeleteView


class UserRegistrationView(FormView):
    form_class = UserRegistrationForm
    template_name = 'app_users/registration.html'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        messages.success(self.request, 'Successfully registered.')
        return redirect('blog-home')


class DeleteAccountView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    success_url = reverse_lazy('login')
    template_name = 'app_users/user_confirm_delete.html'

    # recall UserPassesTestMixin use test_ functions
    def test_func(self):
        user = self.get_object()
        if self.request.user.id == user.id:
            return True
        else:
            return False
