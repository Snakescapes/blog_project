from django.db import models
from blog.models import Article
from imagekit.models import ImageSpecField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToCover


def set_image_save_path(instance, filename):
    return f"{instance.gallery.title}/{filename}"


class Gallery(models.Model):
    article = models.ForeignKey(Article, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return f"Gallery: {self.title}"

    def get_related_images(self):
        related_images = list(self.images.all())
        return related_images

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = 'galleries'


class Image(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='images')
    title = models.CharField(max_length=200)
    size_large = ProcessedImageField(upload_to=set_image_save_path, processors=[ResizeToFill(1600, 900)], format='JPEG', options={'quality': 80}, null=False, blank=False, default='default.jpg')
    size_gallery = ImageSpecField(source='size_large', processors=[ResizeToFill(580, 325)], format='JPEG', options={'quality': 60})
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']

# class Image(models.Model):
#     gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='images')
#     title = models.CharField(max_length=200)
#     image = models.ImageField(default='default.jpg', upload_to=set_image_save_path, null=False, blank=False)
#     timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         ordering = ['-timestamp']