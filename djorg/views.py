from django.shortcuts import render

# Create your views here.
def index(request):
  print('\n\nIndex in djorg\n\n')
  return render(request, 'base.html')