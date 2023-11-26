import requests
from django.conf import settings
from oscarapi.views import checkout

K_INVENTORY_BASE_URL = 'http://localhost:8002/api/' \
    if settings.IS_RUN_IN_DEV_ENV \
    else 'https://ka-be-inventory-iuls6xv2yq-uc.a.run.app/api/'
K_OFFER_BASE_URL = 'http://localhost:8004/api/' \
    if settings.IS_RUN_IN_DEV_ENV \
    else 'https://ka-be-offer-iuls6xv2yq-uc.a.run.app/api/'
K_BASKET_BASE_URL = 'http://localhost:8001/api/' \
    if settings.IS_RUN_IN_DEV_ENV \
    else 'https://ka-be-basket-iuls6xv2yq-uc.a.run.app/api/'


class CheckoutView(checkout.CheckoutView):

    def post(self, request, *args, **kwargs):
        # simulate get basket details
        requests.get(K_BASKET_BASE_URL + 'basket')

        return super().post(request, *args, **kwargs)


class OrderList(checkout.OrderList):

    def get(self, request, *args, **kwargs):
        # simulate get product details
        requests.get(K_INVENTORY_BASE_URL + 'products')

        # simulate get offer details
        requests.get(K_OFFER_BASE_URL + 'offers')

        return super().get(request, *args, **kwargs)


class OrderDetail(checkout.OrderDetail):

    def get(self, request, *args, **kwargs):
        # simulate get product details
        requests.get(K_INVENTORY_BASE_URL + 'products')

        # simulate get offer details
        requests.get(K_OFFER_BASE_URL + 'offers')

        return super().get(request, *args, **kwargs)
