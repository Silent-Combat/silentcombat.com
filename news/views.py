import json
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Posts


def posts(request):
    p = Posts.objects.filter(user=request.user.id)
    print(request.user.id)
    print(p.values())
    return render(request, 'posts.html', {'posts': p})


def delete(request, id):
    p = Posts.objects.filter(id=id).delete()
    return redirect('/')
    

def read(request, id):
    if id >= 1:
        p = Posts.objects.filter(id=id).first()
        return render(request, 'read.html', {'posts': p})


def post(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        if request.user.id is None:
            userid = 'anonymous'
        else:
            userid = request.user.id

        e = Entries.objects.create(
            title=body['title'],
            user=userid,
            entry=body['content'],
        )
        e.save()
        return HttpResponse("success")

    return render(request, 'news.html')