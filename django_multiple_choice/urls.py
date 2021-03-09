"""django_multiple_choice URL Configuration

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
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from core import views
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', views.homepage, name='homepage'),
    path('allusers', views.all_users, name='all-users'),
    path('language/<int:pk>', views.language_page, name='language-page'),
    path('snippet/new', views.add_snippet, name="add-snippet"),
    path('language/new', views.add_language, name="add-language"),
    path('language/<int:pk>/edit', views.edit_language, name="edit-language"),
    path('snippet/<int:pk>/edit', views.edit_snippet, name="edit-snippet"),
    path('snippet/<int:pk>/delete', views.delete_snippet, name="delete-snippet"),
    path('user/<int:pk>', views.user_page, name="user"),
    path('snippet/<int:pk>/copy', views.copy_snippet, name="copy-snippet"),
    path('snippet/<int:pk>/save', views.save_snippet, name="save-snippet"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
