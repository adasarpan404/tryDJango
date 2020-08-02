from django import forms
from .models import blogpost
class BlogPostForm(forms.Form):
    title=forms.CharField()
    slug=forms.SlugField()
    content=forms.CharField(widget=forms.Textarea)

class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model=blogpost
        fields=['title','slug','content']


    def clean_title(self, *args, **kwargs):
        title=self.cleaned_data.get('title')
        qs=blogpost.objects.filter(title__iexact=title)
        if qs.exists():
            raise forms.ValidationError("this title already exists")


        