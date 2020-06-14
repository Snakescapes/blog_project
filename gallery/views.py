from django.shortcuts import render
from .models import Gallery


def gallery_index(request):
    template_name = 'blog/gallery_index.html'
    all_galleries = Gallery.objects.all()
    context = {'galleries': all_galleries}
    return render(request, template_name, context)