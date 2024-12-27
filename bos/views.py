from django.http import HttpResponse
from django.template import loader
# Create your views here.
def bos(request):
  template = loader.get_template('bos.html')
  return HttpResponse(template.render())

def skincare(request):
    template = loader.get_template('skincare.html')
    return HttpResponse(template.render())

def bodycare(request):
    template = loader.get_template('bodycare.html')
    return HttpResponse(template.render())
def combination(request):
    template = loader.get_template('combination.html')
    return HttpResponse(template.render())
def oilyskin(request):
    template = loader.get_template('oilyskin.html')
    return HttpResponse(template.render())
def dryskin(request):
    template = loader.get_template('dryskin.html')
    return HttpResponse(template.render())
def sensitiveskin(request):
    template = loader.get_template('sensitiveskin.html')
    return HttpResponse(template.render())



