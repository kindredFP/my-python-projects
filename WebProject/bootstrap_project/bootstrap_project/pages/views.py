from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = 'home.html'

class CreativeTemplateView(TemplateView):
    template_name = 'creative.html'

class CarouselTemplateView(TemplateView):
    template_name = 'carousel.html'