from django.contrib import admin

from photos.models import Comment, Like, Photo

admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Photo)
