"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from blog.views import (blog_post_detail_page, blog_post_list_view,blog_post_create_view)
from .view import (
    contact_page,
    home_page,
    about_page,
    main_page
)

urlpatterns = [
    url('home_page/', home_page),
    url('contact_page/', contact_page),
    url('about_page/', about_page),
    url('admin/', admin.site.urls),
    url('new/',blog_post_create_view),
    url(r'^blog/(?P<slug>\w+)/$',blog_post_detail_page),
    url('create',main_page),
    url('list',blog_post_list_view)



]
