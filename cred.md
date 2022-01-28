# C2B = Client to Business => Customer is sending money to a paypill (Manual Sim ToolKit)
# Mpesa Express => (Online Payment)


# source ~/documents/venvdaraja/bin/activate

# python manage.py runserver




        """
        {'Body':
            {'stkCallback':
             {
                'CheckoutRequestID': 'ws_CO_DMZ_401669274_11032019190235305',
                'MerchantRequestID': '19927-3244045-1',
                'ResultCode': 0,
                'ResultDesc': 'The service request is processed successfully.',
                'CallbackMetadata': {
                                        'Item': [
                                                {'Name': 'Amount', 'Value': 1.0},
                                                {'Name': 'MpesaReceiptNumber', 'Value': 'NCB1FW1DFZ'},
                                               
                                                {'Name': 'TransactionDate', 'Value': 20190311190244},
                                                {'Name': 'PhoneNumber', 'Value': 254718821114}
                                                ]
                                    }
                                    }
                }
        }
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
