from django.conf.urls import url
from todo import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]