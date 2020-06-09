from django.shortcuts import render
from .models import Gallery


def gallery_index(request):
    template_name = 'blog/gallery_index.html'
    all_galleries = Gallery.objects.all()
    images = []
    for gallery in all_galleries:
        current_gallery_images = list(gallery.images.all())
        images.append(current_gallery_images)
    context = {'galleries': all_galleries, 'images': images}
    return render(request, template_name, context)