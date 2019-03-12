"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf.urls import include
from django.conf import settings
from mainapp import views as mainapp


urlpatterns = [
    url(r'^$', mainapp.main, name='main'),
    url(r'^products/', include(('mainapp.urls', 'mainapp'), namespace='products')),
    url(r'^basket/', include(('basketapp.urls', 'basketapp'), namespace='basket')),
    url(r'^contacts/', mainapp.contacts, name='contacts'),
    url(r'^auth/', include(('authapp.urls', 'authapp'), namespace='auth')),
    url(r'^admin_custom/', include(('adminapp.urls', 'adminapp'), namespace='admin_custom')),
    url('admin/', admin.site.urls, name='admin'),
    # url(r'^', mainapp.main),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
