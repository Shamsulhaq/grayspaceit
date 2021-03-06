"""grayspaceit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from posts.views import posts

from django.views.generic import RedirectView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', RedirectView.as_view(url='/authentication')),
    path('auth/', include('authentication.urls')),
    path('auth/', include('authentication.password.urls')),
    path('profiles/', RedirectView.as_view(url='/profile')),
    path('profile/', include('profiles.urls'), name='profile'),
    path('posts/', include('posts.urls')),
    path('', posts, name='home'),

    # user authentication api
    path('api-token-auth/', obtain_jwt_token),
    path('api/auth/', include('authentication.api.urls')),
    path('api/user/', include('authentication.api.user.urls'))
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
