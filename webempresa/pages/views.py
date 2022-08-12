from django.shortcuts import render, get_object_or_404
from .models import Page

# Create your views here.
def page(reuqest, page_id, page_slug):
    page = get_object_or_404(Page, id=page_id)
    return render(reuqest, 'pages/sample.html',{
        'page':page
    })


