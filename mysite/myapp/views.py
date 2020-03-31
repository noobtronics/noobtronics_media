from django.shortcuts import render
from django.http import HttpResponse
import markdown

def test_view(request):
    context = {}
    text= """
# Table of contents
1. [Introduction](#introduction)
2. [Some paragraph](#paragraph1)
    1. [Sub paragraph](#subparagraph1)
3. [Another paragraph](#paragraph2)

## This is the introduction <a name="introduction"></a>
Some introduction text, formatted in heading 2 style

## Some paragraph <a name="paragraph1"></a>
The first paragraph text

### Sub paragraph <a name="subparagraph1"></a>
This is a sub paragraph, formatted in heading 3 style

## Another paragraph <a name="paragraph2"></a>
The second paragraph text

## Image Test
![](/media/test/django-release-roadmap.png)
![](https://bulma.dev/placeholder/pictures/bg_16-9.svg?primary=00d1b2)
    """
    html = markdown.markdown(text)
    context['html'] = html
    print(html)
    return render(request, 'blog.html', context)
