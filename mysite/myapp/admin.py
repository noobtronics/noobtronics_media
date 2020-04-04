from django.contrib import admin
from myapp.models import *
from django_object_actions import DjangoObjectActions
from django.conf import settings
import markdown
from github import Github
from bs4 import BeautifulSoup



def update_blog_obj(blog_obj):
    g = Github(settings.GITHUB_KEY)
    repo  = g.get_repo("nikhilraut12/electronicspi_media")
    text = repo.get_contents("src/{0}.md".format(blog_obj.slug)).decoded_content.decode()
    html = markdown.markdown(text, extensions=['tables'])
    soup = BeautifulSoup(html)
    h1 = soup.find('h1')
    description = soup.find('p',{'name':'description'})
    blog_obj.title = h1.text
    blog_obj.description = description.text

    h1.decompose()
    description.decompose()

    blog_obj.markdown=text
    blog_obj.html=str(soup)
    blog_obj.save()


class BlogAdmin(DjangoObjectActions, admin.ModelAdmin):
    def update_this(self, request, obj):
        update_blog_obj(obj)
    update_this.label = "Update"  # optional
    update_this.short_description = "Update from Github"  # optional
    change_actions = ('update_this', )

admin.site.register(Blog, BlogAdmin)
