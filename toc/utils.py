# Database Querying
import hashlib
import os

from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class QueryObjects:
    # todo custom related manager

    # todo make query funcs more universal
    @staticmethod
    def query_posts(model, sort_by='desc', order_by='date_posted', **kwargs):
        sort = '-' + str(order_by)
        if sort_by == 'asc':
            sort = str(order_by)
        return model.objects.filter(**kwargs).order_by(sort)

    @staticmethod
    def get_object(model, instance_id):
        return model.objects.get(pk=instance_id)

    @staticmethod
    def get_objects(model, **kwargs):
        return model.objects.filter(**kwargs)

    @staticmethod
    def get_user(user_id):
        return User.objects.get(pk=user_id)

    @staticmethod
    def get_users_excluding(user_id):
        return User.objects.exclude(pk=user_id)


class Pagination:
    @staticmethod
    def paginate_model(request, model_to_paginate_queryset, paginate_by=5):
        paginator = Paginator(model_to_paginate_queryset, paginate_by)
        page = request.GET.get('page', 1)
        try:
            model_to_paginate_queryset = paginator.page(page)
        except (PageNotAnInteger, EmptyPage):
            model_to_paginate_queryset = paginator.page(1)
        return model_to_paginate_queryset


class MediaFiles:
    @staticmethod
    def upload_path(instance, filename):
        hash_md5 = hashlib.md5(instance.image.file.read()).hexdigest()
        ext = instance.image.file.name.split('.')[-1]
        return os.path.join('profile_pics',
                            hash_md5[:2],
                            hash_md5[2:4],
                            f'%s_{instance.pk}.%s' % (hash_md5, ext.lower())
                            )

# forms
#     init
#     create
