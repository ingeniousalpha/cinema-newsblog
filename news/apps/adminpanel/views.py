from django.contrib import auth
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from .models import Admin


def index(request):
    return render(request, 'adminpanel/index.html')


def article_edit_page(request, art_id):
    if request.method == "GET":
        if art_id == 'create':
            return render(request, 'adminpanel/article_edit_page.html', {"article": None})
        art_id = int(art_id)

        try:
            from news.news.apps.articles.models import Article
            a = Article.objects.get(id=art_id)
            print(a)
            article = {}
            article["title"] = a.title
            article["date"] = a.date
            article["image_path"] = a.image_path
            article["text"] = a.text.split('\n')
        except:
            raise Http404("Похоже такой статьи нет...")
        return render(request, 'adminpanel/article_edit_page.html', {"article": article})

    elif request.method == "POST":
        title = request.POST["new_article_title"]
        date = timezone.now()
        image = request.POST["new_article_image"]
        text = request.POST["new_article_text"]
        print(title, image, date, text)
        return HttpResponseRedirect( reverse("index") )


def login_page(request, message=None):
    if request.method == "POST":
        username = request.POST['nickname']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            HttpResponseRedirect(reverse("loginadmin", args=("there is no such user")))
    else:
        return render(request, 'adminpanel/login.html', {"message": message})
