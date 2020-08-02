# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render,get_object_or_404
from .models import blogpost
from .forms import (BlogPostModelForm)

# Create your views here.
def blog_post_detail_page(request,slug):
    obj=get_object_or_404(blogpost, slug=slug)
    template_name="blog_post_detail_page.html"
    context={"object":obj}
    return render(request,template_name,context)

def blog_post_list_view(request):
    qs=blogpost.objects.all()
    template_name="blog_post_list.html"
    context={'object_list':qs}
    return render(request,template_name,context)
@staff_member_required
def blog_post_create_view(request):
    form=BlogPostModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=BlogPostModelForm()
    template_name="blog_post_create.html"
    context={'form':form}
    return render(request,template_name,context)

def blog_post_retrieve_view(request,slug):
    obj=get_object_or_404(blogpost, slug=slug)
    template_name="blog_post_detail.html"
    context={"object":obj}
    return render(request,template_name,context)
def blog_post_update_view(request):
    template_name="blog_post_update.html"
    context={'object_list':[]}
    return render(request,template_name,context)
def blog_post_delete_view(request):
    template_name="blog_post_delete.html"
    context={'object_list':[]}
    return render(request,template_name,context)