from django.urls import include, path

# from rest_framework import routers
from rest_framework_nested import routers
from . import views

# from pprint import pprint

# parent router
router = routers.DefaultRouter()
router.register("products", views.ProductViewSet, basename="products")
router.register("collections", views.CollectionViewSet)

# child router
products_router = routers.NestedDefaultRouter(router, "products", lookup="product")
products_router.register("reviews", views.ReviewerViewSet, basename="product-reviews")

urlpatterns = router.urls + products_router.urls

# urlpatterns = [
#     path('', include(router.urls)),
#     path(),
# ]
