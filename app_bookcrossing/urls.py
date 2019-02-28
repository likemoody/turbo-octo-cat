from django.urls.conf import path

from app_bookcrossing.views import books

urlpatterns = [
    path('bookcrossing/', books.BookShare.as_view(), name='bookcrossing'),
]