from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f'[ {self.pk} '
                f'] {self.title}')

    def urlStr__single_post_page(self):
        return f'/blog/{self.pk}'