from rest_framework.generics import CreateAPIView
from mpesa.api.serializers import LNMOnlineSerializer
from mpesa.models import LNMOnline


from rest_framework.permissions import AllowAny

class LNMCallbackUrlAPIView(CreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        print(request.data,"This is request.data")


        """ 
        {'Body': 
        {'stkCallback': 
        {
            'MerchantRequestID': '14831-6336888-1', 
            'CheckoutRequestID': 
            'ws_CO_280120221124004074', 
            'ResultCode': 0, 
            'ResultDesc': 'The service request is 
            processed successfully.', 
        'CallbackMetadata': {
                              'Item': [
                                  {'Name': 
                                  'Amount',
                                   'Value': 1.0}, 
                                  {'Name': 
                                  'MpesaReceiptNumber', 
                                  'Value': 
                                  'QAS59KSDSR'}, 
                                 {'Name': 
                                 'TransactionDate', 
                                 'Value': 
                                 20220128112530}, 
                                {'Name': 
                                'PhoneNumber', 
                                'Value': 
                                  254799568838}]}}}}
        
         """

        merchant_request_id = request.data["Body"]["stkCallback"]["MerchantRequestID"]
        print(merchant_request_id, "this should be MerchantRequestID")
        checkout_request_id = request.data["Body"]["stkCallback"]["CheckoutRequestID"]
        result_code = request.data["Body"]["stkCallback"]["ResultCode"]
        result_description = request.data["Body"]["stkCallback"]["ResultDesc"]
        amount = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][0][
            "Value"
        ]
        print(amount, "this should be an amount")
        mpesa_receipt_number = request.data["Body"]["stkCallback"]["CallbackMetadata"][
            "Item"
        ][1]["Value"]
        print(mpesa_receipt_number, "this should be an mpesa_receipt_number")

        transaction_date = request.data["Body"]["stkCallback"]["CallbackMetadata"][
            "Item"
        ][3]["Value"]
        print(transaction_date, "this should be an transaction_date")

        phone_number = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][
            4
        ]["Value"]
        print(phone_number, "this should be an phone_number")