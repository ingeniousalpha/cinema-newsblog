from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.utils import dateformat

from .models import Article


def index(request):
    latest = Article.objects.order_by('-date')[0]
    latest.date = latest.date_str()
    articles = Article.objects.all().order_by('-date')[1:]
    for a in articles:
        a.date = a.date_str()
    return render(request, 'articles/index.html', {"latest_article": latest, "articles": articles})


def article_page(request, art_id):
    try:
        a = Article.objects.get(id=art_id)
        article = {
            "title": a.title,
            "date": a.date_str(),
            "image_path": a.image_path,
            "text": a.text.split('\n')
        }
    except:
        raise Http404("Похоже такой статьи нет...")
    return render(request, 'articles/article_page.html', {"article": article})

# return HttpResponseRedirect( reverse("articles:index", args = (id,)))