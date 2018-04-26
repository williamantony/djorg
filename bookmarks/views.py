from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import BookmarkForm
from .models import Bookmark

# Create your views here.
def index(request):
  if request.user.is_anonymous:
    return HttpResponseRedirect(settings.LOGIN_URL)
  if request.method == 'POST':
    form = BookmarkForm(request.POST)
    if form.is_valid():
      form.save()
  context = {
    'bookmarks': Bookmark.objects.all(),
    'form': BookmarkForm(),
  }
  return render(request, 'bookmarks/index.html', context)
  