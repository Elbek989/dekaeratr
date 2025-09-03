from django.contrib import admin
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from configapp.views import (
    ActorApi, ActorDetailApi,
    MovieApi, MovieDetailApi,
    MovieDataAPI,
    CommitApi, CommitDetailApi,
)


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # I
    path('actor/', ActorApi.as_view()),
    path('actor/<int:pk>/', ActorDetailApi.as_view()),


    path('movie/', MovieApi.as_view()),
    path('movie/<int:pk>/', MovieDetailApi.as_view()),


    path('movies/', MovieDataAPI.as_view()),
    path('movies/<int:start_year>/', MovieDataAPI.as_view()),
    path('movies/<int:start_year>/<int:end_year>/', MovieDataAPI.as_view()),


    path('commit/', CommitApi.as_view()),
    path('commit/<int:pk>/', CommitDetailApi.as_view()),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
