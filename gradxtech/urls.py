
from django.contrib import admin
from django.urls import path
from rest_fframework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path
from django.contrib import admin
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.http import JsonResponse

schema_view = get_schema_view(
    openapi.Info(
        title="GradTech API",
        default_version="v1",
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="leanstixx@gmail.com")
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
]
