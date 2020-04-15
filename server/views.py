from django.shortcuts import render

from .models import Servers

def servers(request):
    s = Servers.objects.filter()
    return render(request, 'servers.html', {'servers': s})


def delete(request, id):
    s = Servers.objects.filter(id=id).delete()
    return redirect('/servers')


def server(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        if request.user.id is None:
            return redirect('/servers')
        else:
            s = Servers.objects.create(
                name=body['name'],
                description=body['description'],
                address=body['address'],
            )
            s.save()
            return HttpResponse("Success")
        
        return render(request, 'server.html')


def info(request, id):
    if id >= 1:
        s = Servers.objects.filter(id=id).first()
        return render(request, 'sinfo.html', {'server': s})
