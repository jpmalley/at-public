from django.shortcuts import render
from django.http import JsonResponse
from paypalcheckoutsdk.orders import OrdersCaptureRequest

from .client import PayPalClient
from .models import PayPalTransaction

import json

class CaptureOrder(PayPalClient):
    """Performs payment capture on the order.
    Approved order ID should be passed as an argument to this function"""

    def capture_order(self, order_id, debug=False):
        """Method to capture order using order_id"""
        
        request = OrdersCaptureRequest(order_id)

        # Call PayPal to capture an order
        response = self.client.execute(request)
        result = response.result
        # Save the capture ID to your database. Implement logic to save capture to your database for future reference.
        transaction = PayPalTransaction.objects.create(
            transaction_id=result.id, 
            status=result.status,
            buyer_first_name=result.payer.name.given_name,
            buyer_last_name=result.payer.name.surname,
            buyer_email=result.payer.email_address,
            associated=False,
            )

        # if debug:
        #     print('Status Code: ', response.status_code)
        #     print('Status: ', response.result.status)
        #     print('Order ID: ', response.result.id)
        #     print('Links: ')
        #     for link in response.result.links:
        #         print('\t{}: {}\tCall Type: {}'.format(
        #             link.rel, link.href, link.method))
        #     print('Capture Ids: ')
        #     for purchase_unit in response.result.purchase_units:
        #         for capture in purchase_unit.payments.captures:
        #             print('\t', capture.id)
        #     print("Buyer:")
        #     print("\tEmail Address: {}\n\tName: {}\n\tPhone Number: {}".format(response.result.payer.email_address,
        #                                                                        response.result.payer.name.given_name +
        #                                                                        " " + response.result.payer.name.surname,
        #                                                                        response.result.payer.phone.phone_number.national_number))
        return response

# Create your views here.
def capture_paypal_transaction(request, *args, **kwargs):
    """Captures and saves PayPal transaction via AJAX"""
    request_data = json.load(request)
    order_id = request_data['orderID']
    capture_response = CaptureOrder().capture_order(order_id)
    result = capture_response.result
    response_data = {
        "status":result.status,
        "transaction_id":result.id,
    }
    return JsonResponse(response_data)