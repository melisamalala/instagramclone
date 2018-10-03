from django.shortcuts import render, redirect
from .models import Image,Location,tags
from django.http  import HttpResponse, Http404

# Views
tags = tags.objects.all()

def home_images(request):
    # Display all images here:

    # images = Image.objects.all()

    locations = Location.objects.all()

    if request.GET.get('location'):
        pictures = Image.filter_by_location(request.GET.get('location'))

    elif request.GET.get('tags'):
        pictures = Image.filter_by_tag(request.GET.get('tags'))

    elif request.GET.get('search_term'):
        pictures = Image.search_image(request.GET.get('search_term'))

    else:
        pictures = Image.objects.all()

    return render(request, 'index.html', {'locations':locations,
                                          'tags': tags,
                                          'pictures':pictures})

# Search for an image
def search_image(request):

        # search for an image by the description of the image
        if 'image' in request.GET and request.GET["image"]:
            search_term = request.GET.get("image")
            searched_images = Image.search_image(search_term)
            message = f"{search_term}"

            return render(request, 'search.html', {"message": message, "pictures": searched_images})

        else:
            message = "You haven't searched for any image"
            return render(request, 'search.html', {"message": message})

#         Viewing a single picture
def image(request, id):
    try:
        image = Image.objects.get(pk = id)

    except DoesNotExist:
        raise Http404()

    return render(request, 'image.html', {"image": image})


