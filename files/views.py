from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import FileForm
from .models import File

# Create your views here.
def index(request):
  if request.user.is_anonymous:
    return HttpResponseRedirect(settings.LOGIN_URL)
  if request.method == 'POST':
    form = FileForm(request.POST, request.FILES)
    if form.is_valid():
      instance = File(upload=request.FILES['upload'], name=request.POST['name'])
      instance.save()
      # form.save()
  context = {
    'files': File.objects.all(),
    'form': FileForm(),
  }
  return render(request, 'files/index.html', context)
  