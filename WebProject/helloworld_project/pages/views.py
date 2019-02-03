from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView


# def homePageView(request):
#    return HttpResponse('Hello, World!')

# def catchAllErrorView(request):
#    return HttpResponse('Random Error Page I picked.')

class HomePageView(TemplateView):
    template_name = 'home.html'


class ErrorPageView(TemplateView):
    template_name = 'error.html'


class CatchAllPageView(TemplateView):
    template_name = 'catchAllError.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'

class LandingPageView(TemplateView):
    template_name = 'carousel.html'
