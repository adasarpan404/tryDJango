
from django.shortcuts import render
from .forms import ContactForm
def home_page(request):
    my_title ="hello there......"
    #doc="<h1>{title}<h1>".format(title=my_title)
    #django_rendered_doc="<h1>{{title}}<h1>".format(title=my_title)
    return render(request,"try.html",{"title":my_title})

def about_page(request):
    return render(request,"about.html")

def contact_page(request):
    print(request.POST)
    form=ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form=ContactForm()
    context={
        "title":"contact us",
        "form":form
    }
    return render(request,"form.html",context)
def main_page(request):
    return render(request,"base.html")