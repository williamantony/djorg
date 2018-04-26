from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def index(request):
  if request.user.is_anonymous:
    return HttpResponseRedirect(settings.LOGIN_URL)    
  return render(request, 'djorg_base.html')