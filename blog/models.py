from django.db import models
from django.utils import timezone

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class ArticleCategories(models.Model):
    name = models.CharField(max_length=50)

    @classmethod
    def create_category(cls, new_name):
        new_category = cls(name=new_name)
        return new_category

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "article categories"

class Article(models.Model):
    category = models.ForeignKey(ArticleCategories, on_delete=models.CASCADE)
    title = models.CharField('Article title', max_length=255)
    pub_date = models.DateTimeField('Date published', default=timezone.now)
    image_url = models.CharField('Image url', max_length=2083)
    content = models.TextField('Article content')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['pub_date']

    @classmethod
    def create_article(cls, category, title, pub_date, image_url, content):
        if ArticleCategories.objects.filter(name__icontains=category):
            category = ArticleCategories.objects.filter(name__icontains=category)[0]
        else:
            category = ArticleCategories.create_category(category)
        article = cls(category, title, pub_date, image_url, content)
        return article

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
