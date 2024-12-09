"""
URL configuration for digital_asset_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),


    # Template views
    path('signup/', TemplateView.as_view(template_name="signup.html"), name="signup"),
    path('signin/', TemplateView.as_view(template_name="signin.html"), name="signin"),
    path('dashboard/', TemplateView.as_view(template_name="dashboard.html"), name="dashboard"),
    path('assets/upload/', TemplateView.as_view(template_name="upload_asset.html"), name="upload_asset"),
    path('edit-asset/', TemplateView.as_view(template_name="edit_asset.html"), name="edit_asset"),
    path('categories/', TemplateView.as_view(template_name="categories.html"), name="categories"),
]

