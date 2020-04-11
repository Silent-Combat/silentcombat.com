from django.http import HttpResponse
from django.template.loader import get_template

def index_view(request):
    template = get_template('index.html')
    html = template.render()
    return HttpResponse(html)

def about_view(request):
    template = get_template('about.html')
    html = template.render()
    return HttpResponse(html)

def rules_view(request):
    template = get_template('rules.html')
    html = template.render()
    return HttpResponse(html)

def donate_view(request):
    template = get_template('doante.html')
    html = template.render()
    return HttpResponse(html)
