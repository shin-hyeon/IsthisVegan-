"""config URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from ckeditor_uploader import views as views_ckeditor
from django.views.decorators.cache import never_cache
import users.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("posts.urls")),
    path("core/", include("core.urls")),
    path("users/", include("users.urls")),
    path("askproduct/", include("reports.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("upload/", login_required(views_ckeditor.upload), name="ckeditor_upload"),
    path(
        "browse/",
        never_cache(login_required(views_ckeditor.browse)),
        name="ckeditor_browse",
    ),
    path("accounts/", include("allauth.urls")),
    path("search_prd/", include("search.urls")),
    path(
        "serviceWorker.js",
        (
            TemplateView.as_view(
                template_name="serviceWorker.js",
                content_type="application/javascript",
            )
        ),
        name="serviceWorker.js",
    ),
    path(
        "firebase-messaging-sw.js",
        (
            TemplateView.as_view(
                template_name="firebase-messaging-sw.js",
                content_type="application/javascript",
            )
        ),
        name="firebase-messaging-sw.js",
    ),
    path("notifications/", include("notifications.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
