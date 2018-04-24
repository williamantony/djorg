from django.shortcuts import render

from .forms import NoteForm
from .models import Note

# Create your views here.
def index(request):
  if request.method == 'POST':
    form = NoteForm(request.POST)
    if form.is_valid():
      profile = form.save(commit=False)
      profile.user = request.user
      profile.save()
  context = {
    'notes': Note.objects.all(),
    'form': NoteForm(),
  }
  return render(request, 'notes/index.html', context)
  