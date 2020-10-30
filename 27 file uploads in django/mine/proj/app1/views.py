from django.shortcuts import render
from .models import File
from .forms import FileForm


def showfile(request):

    lastfile = File.objects.last()

    filepath = lastfile.filepath

    filename = lastfile.name

    form = FileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context = {'filepath': filepath,
               'form': form,
               'filename': filename
               }

    return render(request, 'Blog/files.html', context)
