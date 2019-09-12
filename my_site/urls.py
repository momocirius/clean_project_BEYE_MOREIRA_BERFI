"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path

from .views import home_page_view, home_page_view_with_render, form, \
page_needing_js, show_image, profile, skeleton, using_skeleton


urlpatterns = [
    #Chemin entre l'URL et la vue.
    path('admin/', admin.site.urls),
    path('log', home_page_view, name='home'),
    path('home/', home_page_view_with_render, name="home_render"),
    path('profile/<int:question_int>/', profile),
    path('', auth_views.LoginView.as_view(), name='login'),
]
