from django.urls import path
from .views import (
    LogCreate,
    LogList,
    LogUpdate,
    LogDelete,
    ZoneConnectionCreate,
    ZoneConnectionList,
    Puzzle,
)
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view  # type: ignore
from drf_yasg import openapi  # type: ignore


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("log-create/", LogCreate.as_view(), name="log_create"),
    path("puzzle/", Puzzle.as_view(), name="puzzle"),
    path("log-list/", LogList.as_view(), name="log_list"),
    path("log-update/<int:pk>/", LogUpdate.as_view(), name="log_update"),
    path("log-delete/<int:pk>/", LogDelete.as_view(), name="log_delete"),
    path(
        "zone-connection-create/",
        ZoneConnectionCreate.as_view(),
        name="zone_connection_create",
    ),
    path(
        "zone-connection-list/",
        ZoneConnectionList.as_view(),
        name="zone_connection_list",
    ),
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
