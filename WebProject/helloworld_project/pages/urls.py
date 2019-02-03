from django.urls import path, re_path


from . import views

urlpatterns = [
    # path('', views.homePageView, name='home'), # this is original way using methods on view.py
    # path('newURL', views.homePageView, name='home'),  # added this to navigate somewhere else
    # path('\S\S', views.catchAllErrorView, name='error')  # need to work on this

    path('', views.HomePageView.as_view(), name='home'),
    path('error', views.ErrorPageView.as_view(), name='error'),
    path('about', views.AboutPageView.as_view(), name='about'),
    path('index', views.LandingPageView.as_view(), name='index'),
    re_path('\S+', views.CatchAllPageView.as_view()),

]
