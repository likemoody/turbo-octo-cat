from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.utils.translation import gettext as _

from app_blog.models import Post
from ..forms import UserUpdateForm, ProfileUpdateForm
from toc.utils import QueryObjects, Pagination

from django.contrib.auth import update_session_auth_hash


class UserProfileView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        queryset = QueryObjects.query_posts(Post, blocked=False, author_id=user_id)
        queryset = Pagination.paginate_model(request, queryset)
        user_profile = QueryObjects.get_user(user_id)
        return render(request, 'app_users/profile_view.html', locals())


class UserProfileEditView(LoginRequiredMixin, View):
    def get(self, request):
        user_profile = QueryObjects.get_user(request.user.id)
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user)
        return render(request, 'app_users/profile_edit.html', locals())

    def post(self, request):
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.add_message(request, messages.SUCCESS, _('Profile updated successfully'))
            return redirect('profile', request.user.id)
        return redirect('my-profile-edit')


class UserChangePasswordView(LoginRequiredMixin, View):
    def get(self, request):
        user_profile = QueryObjects.get_user(request.user.id)
        password_form = PasswordChangeForm(request.user)
        return render(request, 'app_users/profile_edit.html', locals())

    def post(self, request):
        # fixme password change issue
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, _('Password has been changed successfully'))
            return redirect('profile', request.user.id)
        messages.add_message(request, messages.ERROR, _('Error occurred'), extra_tags='danger')
        return redirect('profile', request.user.id)
