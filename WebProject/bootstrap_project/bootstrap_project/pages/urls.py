from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('carousel', views.CarouselTemplateView.as_view(), name='carousel'),
    path('creative', views.CreativeTemplateView.as_view(), name='creative'),
]