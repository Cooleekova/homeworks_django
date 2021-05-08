from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Scope, ArticleScope


def articles_list(request):
    template = 'articles/news.html'
    context = {}
    articles = Article.objects.all().order_by('-published_at').prefetch_related('scopes')
    news = list(articles)
    context['object_list'] = news
    return render(request, template, context)


# ArticleScope.objects.filter(is_main=True)
