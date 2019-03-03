from django.urls import path
from app_blog.views import home, posts, messages

urlpatterns = [
    path('', home.HomeView.as_view(), name='blog-home'),
    path('post-create/', posts.CreatePostView.as_view(), name='create-post'),
    path('post-edit/<int:post_id>/', posts.EditPostView.as_view(), name='edit-post'),
    path('post/<int:post_id>/', posts.PostDetailsView.as_view(), name='post'),

    path('send-message/', messages.SendMessageView.as_view(), name='send-message'),
    path('send-message/<int:user_id>/', messages.SendMessageToView.as_view(), name='send-message-to'),
    path('conversations/', messages.ConversationsView.as_view(), name='conversations'),
    path('message/<int:message_id>/', messages.SingleMessageView.as_view(), name='message'),
]
