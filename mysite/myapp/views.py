from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings





def test_view(request):
    context = {}
    text = repo.get_contents("README.md").decoded_content.decode()
    context['html'] = html
    print(html)
    return render(request, 'blog.html', context)
