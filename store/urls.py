from django.urls import include, path
from rest_framework.routers import SimpleRouter
from . import views

# from pprint import pprint


router = SimpleRouter()
router.register("products", views.ProductViewSet)
router.register("collections", views.CollectionViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     path('', include(router.urls)),
#     path(),
# ]
