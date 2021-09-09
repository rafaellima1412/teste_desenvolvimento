"""webapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from microservico import views
from microservico.api.routers import router as micro_router
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="swagger-microserviço")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(micro_router.urls)),
    path("me/", views.mine),
    path("doc/", schema_view),
]
