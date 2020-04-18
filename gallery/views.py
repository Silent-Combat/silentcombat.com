from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Gallery
from .forms import ImageUpload


def gallery(request):
    g = Gallery.objects.filter()
    return render(request, 'gallery.html', {'gallery': g})


def upload(request):
    if request.method == 'POST':
        form = ImageUpload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/gallery')
    else:
        form = ImageUpload()
    
    return render(request, 'upload.html', {'form': form})


def info(request, id):
    if id >= 1:
        g = Gallery.objects.filter(id=id).first()
        return render(request, 'gimage.html', {'gallery': s})
