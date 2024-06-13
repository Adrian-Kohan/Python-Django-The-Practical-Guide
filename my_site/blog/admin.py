from django.contrib import admin
from .models import Posts, Tag, Author, Comment

# Register your models here.
class PostsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "author", "date")
    list_filter = ("author", "date", "tag")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("username", "post")

admin.site.register(Posts, PostsAdmin)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Comment, CommentAdmin)


