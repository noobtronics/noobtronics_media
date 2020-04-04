from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from myapp.views import *
from django.shortcuts import get_list_or_404, get_object_or_404
from myapp.models import *


def test_view(request):
    context = {}
    text = repo.get_contents("README.md").decoded_content.decode()
    context['html'] = html
    print(html)
    return render(request, 'blog.html', context)



def blog_view(request, slug):
    blog_obj = get_object_or_404(Blog, slug=slug)
    context = {
        'title': blog_obj.title,
        'heading': blog_obj.heading,
        'description': blog_obj.description,
        'html': blog_obj.html,
    }
    return render(request, 'blog.html', context)


def minidatasheet_view(request, ic_name):
    slug = '/minidatasheet/{0}'.format(ic_name)
    return blog_view(request, slug)
