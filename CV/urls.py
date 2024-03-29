"""
URL configuration for CV project.

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
from django.contrib import admin
from django.urls import path, include
from web.views import *
from api.views import *
from django.conf.urls.static import static
from django.conf import settings
from web.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cvs/', cv_list, name='cv_list'),
    # path('cvs/<int:cv_id>/', cv_detail, name='cv_detail'),
    path('api/cv-detail/<int:cv_id>/', CVDetailView.as_view(), name='cv_detail_api'),
    path('api/', include('api.urls')),
    # path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('cv1/<int:cv_id>/', cv_detail_1, name='cv_detail_1'),
    path('cv2/<int:cv_id>/', cv_detail_2, name='cv_detail_2'),
    path('cv3/<int:cv_id>/', cv_detail_3, name='cv_detail_3'),
    path('cv4/<int:cv_id>/', cv_detail_4, name='cv_detail_4'),
    path('cv5/<int:cv_id>/', cv_detail_5, name='cv_detail_5'),
    path('cv6/<int:cv_id>/', cv_detail_6, name='cv_detail_6'),
    path('cv7/<int:cv_id>/', cv_detail_7, name='cv_detail_7'),
    path('cv8/<int:cv_id>/', cv_detail_8, name='cv_detail_8'),
    path('cv9/<int:cv_id>/', cv_detail_9, name='cv_detail_9'),
    path('cv10/<int:cv_id>/', cv_detail_10, name='cv_detail_10'),
    path('api/cv-detail/<int:cv_id>/', CVDetailView.as_view(), name='cv_detail_api'),
]
# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
