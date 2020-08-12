import os
from django.contrib import auth
from django.http import Http404, HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.apps import apps
Article = apps.get_model('articles', 'Article')


def index(request):
    if request.method == "POST":
        id = request.POST['modal_value']
        a = Article.objects.get(id=id)
        a.delete()
    articles = Article.objects.all().order_by('-date')
    for a in articles:
        a.date = a.date_str()
    amount = len(articles)
    return render(request, 'adminpanel/index.html', {"articles": articles, "amount": amount})


def article_edit_page(request, art_id):
    if request.method == "GET":
        if art_id == 'create':
            return render(request, 'adminpanel/article_edit_page.html', {"article": None})

        art_id = int(art_id)
        try:
            a = Article.objects.get(id=art_id)
            a.date = a.date_str()
        except:
            raise Http404("Похоже такой статьи нет...")
        return render(request, 'adminpanel/article_edit_page.html', {"article": a})

    elif request.method == "POST":
        title = request.POST["new_article_title"]
        image = None
        if 'new_article_image' in request.FILES:
            image = request.FILES['new_article_image']
        text = request.POST["new_article_text"]

        # print(title, image.name, date, text)
        if art_id == 'create':
            date = timezone.now()
            a = Article(title=title, date=date, text=text)
            a.save()
        else:
            a = Article.objects.get(id=art_id)
            a.title = title
            a.text = text
            a.save()
        print(a)

        if image is not None:
            image_name = "article" + str(a.id) + os.path.splitext(image.name)[-1]

            # uploading file
            with open("news/apps/articles/static/images/"+image_name, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)
            a.image_path = 'images/' + image_name
            a.save()
        return HttpResponseRedirect( reverse("index") )


def article_date_update(request, art_id):
    a = Article.objects.get(id=art_id)
    date = timezone.now()
    a.date = date
    a.save()
    mydate = a.date_str()
    return JsonResponse({"date": mydate})


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
