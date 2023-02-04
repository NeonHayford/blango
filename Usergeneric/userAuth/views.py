from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers, vary_on_cookie
from rest_framework.exceptions import PermissionDenied
# Create your views here.

@method_decorator(cache_page(300))
@method_decorator(vary_on_headers("Authorization"))
@method_decorator(vary_on_cookie)
@action(methods=["get"], detail=False, name="Posts by the logged in user")
def mine(self, request):
    if request.user.is_anonymous:
        raise PermissionDenied("You must be logged in to see which Posts are yours")
    posts = self.get_queryset().filter(author=request.user)
    serializer = PostSerializer(posts, many=True, context={"request": request})
    return Response(serializer.data)

@method_decorator(cache_page(120))
def list(self, *args, **kwargs):
    return super(PostViewSet, self).list(*args, **kwargs)


@method_decorator(cache_page(300))
def get(self, *args, **kwargs):
    return super(UserDetail, self).get(*args, *kwargs)


@method_decorator(cache_page(300))
def list(self, *args, **kwargs):
    return super(TagViewSet, self).list(*args, **kwargs)

@method_decorator(cache_page(300))
def retrieve(self, *args, **kwargs):
    return super(TagViewSet, self).retrieve(*args, **kwargs)
