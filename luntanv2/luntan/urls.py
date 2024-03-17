"""luntan URL Configuration

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
from django.contrib import admin
from django.urls import path, include, re_path
from django.views import static
import os
from django.conf import settings
from django.conf.urls.static import static as s2

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('login.html', views.login_html, name='login'),
    path('detail.html', views.detail_html, name='detail'),
    path('blogDetail.html', views.blogDetail_html, name='blog_detail'),
    path('footer.htm', views.footer_html, name='footer'),
    path('header.htm', views.header_html, name='header'),
    path('index.html', views.index_html, name='index'),
    path('', views.index_html, name='index'),
    path('nationDetail.html', views.nationDetail_html, name='nation_detail'),
    path('places.html', views.places_html, name='places'),
    path('pushBlog.html', views.pushBlog_html, name='push_blog'),
    path('signup.html', views.signup_html, name='signup'),
    path('user.html', views.user_html, name='user'),
    path('user_profile.html', views.user_profile_html, name='user_profile'),
    re_path(r'^static/(?P<path>.*)$', static.serve, {'document_root': os.path.join(BASE_DIR, 'static')}),
]
urlpatterns += s2(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
