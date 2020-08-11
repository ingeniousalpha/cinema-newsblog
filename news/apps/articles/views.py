from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Article


def index(request):
    latest = Article.objects.order_by('-date')[0]
    articles = Article.objects.all().order_by('-date')[1:]
    return render(request, 'articles/index.html', {"latest_article": latest, "articles": articles})


def article_page(request, art_id):
    try:
        a = Article.objects.get(id=art_id)
        article = {}
        article["title"] = a.title
        article["date"] = a.date
        article["image_path"] = a.image_path
        article["text"] = a.text.split('\n')
    except:
        raise Http404("Похоже такой статьи нет...")
    return render(request, 'articles/article_page.html', {"article": article})

# return HttpResponseRedirect( reverse("articles:index", args = (id,)))