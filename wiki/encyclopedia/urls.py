from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("CSS", views.entry, name="entry"),
    path("random", views.random_entry, name="random")
]
