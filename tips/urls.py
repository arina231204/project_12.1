from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from drf_yasg import openapi

from interview import views

schema_view = get_schema_view(
   openapi.Info(
      title="Twitter Clone API",
      default_version='v-0.01-alpha',
      description="API для взаимодействия с Twitter API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="arinaten23@gmail.com"),
      license=openapi.License(name="No Licence"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register('category', views.CategoryViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/categories/', views.CategoryListCreateAPIView.as_view()),
    path('api/', include(router.urls)),
    path('api/question/', views.QuestionListCreateAPIView.as_view()),
    path('api/question/<int:pk>/', views.QuestionDetailDeleteUpdate.as_view()),
    path('swagger/', schema_view.with_ui('swagger'),  name='swagger_doc'),
]
