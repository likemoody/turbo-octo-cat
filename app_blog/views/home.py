from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from ..models import Post

from toc.utils import QueryObjects, Pagination
from django.shortcuts import render
from django.views.generic.base import View


class HomeView(View):
    def get(self, request):
        queryset = QueryObjects.query_posts(Post, blocked=False)
        queryset = Pagination.paginate_model(request, queryset)

        return render(request, 'app_blog/home.html', locals())
