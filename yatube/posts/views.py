from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from constants import PAGE_LIMIT


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.select_related('author')[:PAGE_LIMIT]
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_list(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.select_related('author')[:PAGE_LIMIT]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
