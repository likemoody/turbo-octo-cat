from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from ..models import Book


class BookShare(LoginRequiredMixin, ListView):
    model = Book
    queryset = Book.objects.all()
    template_name = 'app_bookcrossing/books_view.html'
