from django.contrib import admin
from .models import Post, Author, Tag, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content', 'author__first_name', 'author__last_name')
    list_filter = ('date', 'author', 'tags')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','post')


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)

