from django.db import models
from django.utils import timezone
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


def set_image_save_path(instance, filename):
    return f"{instance.title}/{filename}"


class ArticleCategories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "article categories"


class Article(models.Model):
    category = models.ForeignKey(ArticleCategories, on_delete=models.CASCADE)
    title = models.CharField('Article title', max_length=255)
    pub_date = models.DateTimeField('Date published', default=timezone.now)
    content = models.TextField('Article content')
    status = models.IntegerField(choices=STATUS, default=0)
    carousel_img = ProcessedImageField(upload_to=set_image_save_path, processors=[ResizeToFill(1100, 400)], format='JPEG', options={'quality': 80}, null=False, blank=False, default='default.jpg')
    cover_img = ImageSpecField(source='carousel_img', processors=[ResizeToFill(280, 160)], format='JPEG', options={'quality': 80})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    class Meta:
        ordering = ['-created_on']


