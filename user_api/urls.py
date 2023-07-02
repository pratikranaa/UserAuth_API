"""
URL configuration for user_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework_simplejwt import views as jwt_views
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from django.conf import settings
from django.conf.urls.static import static
from login_api.views import UserLoginView

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="ERP System API",
        default_version='1.0.0',
        description="API documentation of App",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),
    path('api/',include('login_api.urls')),
    path('api/login/', UserLoginView.as_view(), name='token_obtain_pair'),
    path('api/login-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/login-verify/', jwt_views.TokenVerifyView.as_view(), name='verify_token'),
]
