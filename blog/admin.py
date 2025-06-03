from django.contrib import admin
from .models import Post

# admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ('custom_title', 'updated_at', 'created_at')

    list_display_links = ('custom_title',)

    def custom_title(self, obj):
        return f"[{obj.pk}] {obj.title}"

    custom_title.short_description = "목차"
    Post._meta.get_field('updated_at').verbose_name = "수정일"
    Post._meta.get_field('created_at').verbose_name = "등록일"

admin.site.register(Post, PostAdmin)