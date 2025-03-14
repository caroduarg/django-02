from django.urls import path
from website.views import AboutPageView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('about/', AboutPageView.as_view(), name = 'about'),
]