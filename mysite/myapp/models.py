from django.db import models



class Blog(models.Model):
    slug = models.CharField(max_length=200)
    title = models.CharField(max_length=200, null=True, blank=True)
    heading = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    markdown = models.TextField(null=True, blank=True)
    html = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug
