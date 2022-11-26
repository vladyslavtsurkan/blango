from django.contrib import admin

from blog.models import Tag, Post, Comment


class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('title', )}
  list_display = ('title', 'slug', 'published_at')


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
