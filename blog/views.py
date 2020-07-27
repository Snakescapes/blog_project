from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from .models import Article
from .forms import CommentForm


# Class-based views:

class ArticleListView(ListView):
    model = Article
    template_name = "blog/index.html" # <app>/<model>_<viewtype>.html
    ordering = ['pub_date']

    def get_context_data(self, *, object_list=None, **kwargs):
        article_1, article_2, article_3 = self.get_queryset().order_by('-pub_date')[:3]
        context = {'all_articles': self.get_queryset(), 'article_1': article_1, 'article_2': article_2, 'article_3': article_3}
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = "detail.html"
    new_comment = None

    def get_context_data(self, **kwargs):
        article = self.get_object()
        comment_form = CommentForm()
        comments = article.comments.filter(active=True)
        context = {
            'article': article,
            'comments': comments,
            'new_comment': self.new_comment,
            'comment_form': comment_form
        }
        return context

    def post(self, request, **kwargs):
        article = self.get_object()
        comments = article.comments.filter(active=True)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = self.get_object()
            new_comment.save()
        context = {
            'article': article,
            'comments': comments,
            'new_comment': self.new_comment,
            'comment_form': comment_form
        }
        return render(request, self.template_name, context)


# Function-based views:

# def index(request):
#     all_articles = Article.objects.all().order_by('pub_date')[:6]
#     article_1, article_2, article_3 = Article.objects.all().order_by('-pub_date')[:3]
#     context = {'all_articles': all_articles, 'article_1': article_1, 'article_2': article_2, 'article_3': article_3}
#     return render(request, 'blog/index.html', context)


# def detail(request, article_id):
#     current_article = get_object_or_404(Article, pk=article_id)
#     template_name = 'blog/detail.html'
#     comments = current_article.comments.filter(active=True)
#     new_comment = None
#     if request.method == "POST":
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.article = current_article
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#
#     return render(request, template_name, {
#                                             'article': current_article,
#                                             'comments': comments,
#                                             'new_comment': new_comment,
#                                             'comment_form': comment_form
#                                                                         })


