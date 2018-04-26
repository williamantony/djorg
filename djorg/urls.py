"""djorg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from graphene_django.views import GraphQLView
from rest_framework import routers
from notes.api import NoteViewSet

from .views import index as homepage_view

router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path('', homepage_view, name='index'),
    path('bookmarks/', include('bookmarks.urls')),
    path('notes/', include('notes.urls')),
    path('files/', include('files.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api/', include(router.urls)),
    path('graphql/', GraphQLView.as_view(graphiql = True)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
