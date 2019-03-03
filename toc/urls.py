"""toc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from .settings import *

from app_blog.views import api
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    # path('', include('app_blog.urls')),
    # path('', include('app_users.urls')),
    path('api-posts/', api.PostList.as_view(), name='api-posts'),
    path('api-posts/<int:pk>/', api.PostSingle.as_view(), name='api-post'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += i18n_patterns(
    path('', include('app_blog.urls')),
    path('', include('app_users.urls')),
    path('', include('app_bookcrossing.urls')),
    prefix_default_language=True,
)

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
