from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import ArticleCategories, Article
from .forms import CommentForm


def index(request):
    all_articles = Article.objects.all()
    article_1, article_2, article_3 = Article.objects.all().order_by('-pub_date')[:3]
    context = {'all_articles': all_articles, 'article_1': article_1, 'article_2': article_2, 'article_3': article_3}
    return render(request, 'blog/index.html', context)


def detail(request, article_id):
    current_article = get_object_or_404(Article, pk=article_id)
    template_name = 'blog/detail.html'
    comments = current_article.comments.filter(active=True)
    new_comment = None
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = current_article
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {
                                            'article': current_article,
                                            'comments': comments,
                                            'new_comment': new_comment,
                                            'comment_form': comment_form
                                                                        })




    # form = CommentForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    #     form = CommentForm()
    # context = {'form': form, 'article': current_article}
    # return render(request, 'blog/detail.html', context)


# def categories(request):

# def add_comment(request):
#     form = CommentForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#
#     context = {'form': form}
#     return render(request, 'blog/detail.html', {'context': context})
