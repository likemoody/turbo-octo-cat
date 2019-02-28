import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic.edit import CreateView
from django.utils.translation import gettext as _

from toc.utils import QueryObjects
from ..forms import AddCommentForm, EditPostForm
from ..models import Post, Comment


class CreatePostView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'app_blog/create_post.html'
    success_message = _('Post has been created')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailsView(View):
    def get(self, request, post_id):
        add_comment_form = AddCommentForm()
        post = QueryObjects.get_object(Post, post_id)
        return render(request, 'app_blog/post_view.html', locals())

    def post(self, request, post_id):
        add_comment_form = AddCommentForm(request.POST)
        if add_comment_form.is_valid():
            content = add_comment_form.cleaned_data.get('content')
            date_posted = datetime.datetime.now()
            author = QueryObjects.get_user(request.user.id)
            Comment.objects.create(content=content,
                                   date_posted=date_posted,
                                   author=author,
                                   post_id=post_id)
        return redirect('post', post_id=post_id)


class EditPostView(LoginRequiredMixin, View):
    # recall, full potential of dispatch()
    # snippet
    def dispatch(self, request, *args, **kwargs):
        author = QueryObjects.get_object(Post, kwargs.get('post_id')).author

        if request.method == "GET":
            if author == request.user:
                return self.get(request, *args, **kwargs)
            else:
                return redirect('blog-home')
        elif request.method == "POST":
            return self.post(request, *args, **kwargs)

    def get(self, request, post_id):
        post = QueryObjects.get_object(Post, post_id)
        post_edit_form = EditPostForm(instance=post)
        return render(request, 'app_blog/post_edit.html', locals())

    def post(self, request, post_id):
        post_edit_form = EditPostForm(request.POST)
        if post_edit_form.is_valid():
            title = post_edit_form.cleaned_data.get('content')
            content = post_edit_form.cleaned_data.get('title')
            post = QueryObjects.get_object(Post, post_id)
            post.title = title
            post.content = content
            post.last_edited_on = datetime.datetime.now()
            post.save()
        return redirect('post', post_id=post_id)
