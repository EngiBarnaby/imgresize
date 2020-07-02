from django.shortcuts import render
from .forms import UserImageForm


def convert_img(request):
    if request.method == "GET":
        form = UserImageForm()
        context = {"form": form}
        return render(request, 'resize/main-page.html', context)
    else:
        image_type = request.FILES['image']
        image_type = str(image_type).split('.')[-1]
        form = UserImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.type = image_type
            form = form.save()
            context = {'form' : form}
            return render(request, 'resize/result.html', context)
