from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # TODO: change `admin` to more complicated path e.g. `hard-to-guess-path-to-admin`
    path('admin/', admin.site.urls),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    # Test view for base.html
    path('', TemplateView.as_view(template_name='base.html'), name='base'),
    path("users/", include("django_chat.users.urls", namespace="users")),
    path('i18n/', include('django.conf.urls.i18n')),
    # API base url
    path("api/", include("config.api_router")),
    # DRF auth token
    path("auth-token/", obtain_auth_token),
]

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('rosetta/', include('rosetta.urls'))
    ]

if settings.DEBUG and 'debug_toolbar' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('debug_toolbar/', include('debug_toolbar.urls')),
    ]

# API documentation in Swagger or ReDoc
if 'drf_yasg' in settings.INSTALLED_APPS:
    schema_view = get_schema_view(
        openapi.Info(
            title="django_chat API",
            default_version='v1',
            description="Rest APi for Django django_chat template",
            contact=openapi.Contact(email="author@email.com"),
            license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=[permissions.AllowAny],
    )

    urlpatterns += [
        re_path(
            r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'
        ),
        path(
            'swagger/',
            schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'
        ),
        path(
            'redoc/',
            schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'
        ),
    ]
