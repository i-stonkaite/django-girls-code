from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    posts = Post.objects.filter().order_by('published_date').all()
    return render(request, 'blog/post_list.html', {'posts': posts})
