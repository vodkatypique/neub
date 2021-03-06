"""neub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.conf.urls.static import static
from django.conf import settings
from .routers import router


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/v1/auth/obtain_token/', obtain_jwt_token),
    path('^api/v1/auth/refresh_token/', refresh_jwt_token),
    #
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(                            # add this
            settings.STATIC_URL,
            document_root=settings.STATIC_ROOT
          )
    urlpatterns += static(                            # add this
            settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)
