from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("logout", views.logout_view, name="logout"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("forum", views.forum, name="forum"),
    path("demo", views.demo, name="demo"),
    path("share", views.share, name="share"),
    path("new_post", views.new_post, name="new_post"),
    path("layout", views.layout, name="layout"),
    path("new_layout", views.new_layout, name="new_layout"),
    path("features", views.features, name="features")
]
