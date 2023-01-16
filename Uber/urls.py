from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from account import views as acc_view
from service import views as ser_view
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

acc_router = DefaultRouter()
acc_router.register('register', acc_view.ProfileRegisterAPIView)

posts_router = DefaultRouter()
posts_router.register('taxi', ser_view.TaxiListAPIView)
posts_router.register('order', ser_view.OrderViewSet)
# posts_router.register('rating', ser_view.RatingViewSet)

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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/accounts/', include(acc_router.urls)),
    path('api/service/', include(posts_router.urls)),
    path('api/account/rating/<int:pk>/', ser_view.StatusDriverViewSet.as_view({'post': 'rate_driver'})),
    path('api/account/status_type/', ser_view.StatusTypeViewSet.as_view({'get': 'list'})),
    path('api/account/status_driver/', ser_view.StatusDriverViewSet.as_view({'get': 'list'})),
    path('swagger/', schema_view.with_ui('swagger'),  name='swagger_doc' ),
]

