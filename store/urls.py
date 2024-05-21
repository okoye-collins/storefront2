from django.urls import include, path

# from rest_framework import routers
from rest_framework_nested import routers
from . import views

# from pprint import pprint

# parent router
router = routers.DefaultRouter()
router.register("products", views.ProductViewSet, basename="products")
router.register("collections", views.CollectionViewSet)
router.register("carts", views.CartViewSet)
router.register("customers", views.CustomerViewSet)
router.register("orders", views.OrderViewSet, basename="orders")

# product child router
products_router = routers.NestedDefaultRouter(router, "products", lookup="product")
products_router.register("reviews", views.ReviewerViewSet, basename="product-reviews")

# cart child router
carts_router = routers.NestedDefaultRouter(router, 'carts', lookup="cart")
carts_router.register("items", views.CartItemViewSet, basename="cart-items")

urlpatterns = router.urls + products_router.urls + carts_router.urls

