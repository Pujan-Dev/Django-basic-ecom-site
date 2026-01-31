
from rest_framework import routers
from .views import CategoryViewSet, ProductViewSet, OrderViewSet
from .user_views import UserRegisterView
from django.urls import path

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
	path('auth/register/', UserRegisterView.as_view(), name='user-register'),
]
urlpatterns += router.urls
