from rest_framework import routers
from .views import *

#? Initialize a DefaultRouter instance from DRF
router = routers.DefaultRouter()

#? Register the CategoryAPI viewset with the router under the URL 'categories'
router.register(r"categories", CategoryAPI)

#? Register the ProductAPI viewset with the router under the URL 'products'
router.register(r"products", ProductAPI)

#? Register the CartAPI viewset with the router under the URL 'carts'
router.register(r"carts", CartAPI)

#? Register the BuyAPI viewset with the router under the URL 'buys'
router.register(r"buys", BuyAPI)

#? Generate the urlpatterns based on the registered routes
urlpatterns = router.urls
