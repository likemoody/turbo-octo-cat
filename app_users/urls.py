from django.urls.conf import path
from .views import profile, auth
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile/<int:user_id>/', profile.UserProfileView.as_view(), name='profile'),
    path('profile-edit/', profile.UserProfileEditView.as_view(), name='my-profile-edit'),
    path('password-change/', profile.UserChangePasswordView.as_view(), name='password-change'),
    path('login/', auth_views.LoginView.as_view(template_name='app_users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='app_users/logout.html'), name='logout'),
    path('registration/', auth.UserRegistrationView.as_view(), name='registration'),
    path('account-delete/<int:pk>/', auth.DeleteAccountView.as_view(), name='account-delete'),
]
