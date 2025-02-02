# """
# URL configuration for hello project.
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.conf import settings
# from django.contrib import admin
# from django.contrib.messages import api
# from django.urls import path, include
# from django.conf.urls.static import static
#
# api_routers = [
#     path('v1/', include('api_v1.urls')),
#     path('v2/', include('api_v2.urls')),
# ]
#
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include("webapp.urls")),
#     path('accounts/', include("accounts.urls")),
#     path('api/', include(api_routers)),
#
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


"""
URL configuration for hello project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

# Определяем маршруты для API версий
api_routers = [
    path('v1/', include('api_v1.urls')),
    path('v2/', include('api_v2.urls')),
]

urlpatterns = [
                  # Административные панели
                  path('admin/', admin.site.urls),

                  # Основной сайт
                  path('', include("webapp.urls")),

                  # Управление пользователями
                  path('accounts/', include("accounts.urls")),

                  # API
                  path('api/', include(api_routers)),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
