import random
import requests
import json
import time
import uuid

class WaafiPayClient:
    def __init__(self, merchant_uid, api_user_id, api_key):
        self.merchant_uid = merchant_uid
        self.api_user_id = api_user_id
        self.api_key = api_key
        self.base_url = "https://api.waafipay.net/asm"
        self.request_id = None  # Initialize request_id
        self.timestamp = None    # Initialize timestamp
        self.invoice_id = None    # Initialize invoice_id

    def preauthorize_payment(self, payer_account, amount, currency="USD", description="test"):
        # Generate unique requestId and referenceId
        self.request_id = str(uuid.uuid4())
        reference_id = str(uuid.uuid4())

        self.invoice_id = random.randint(10000, 99999)

        # Get current timestamp
        self.timestamp = int(time.time())

        # Prepare the request payload
        payload = {
            "schemaVersion": "1.0",
            "requestId": self.request_id,  # Unique requestId
            "timestamp": self.timestamp,     # Current timestamp
            "channelName": "WEB",
            "serviceName": "API_PREAUTHORIZE",
            "serviceParams": {
                "merchantUid": self.merchant_uid,  # Merchant UID
                "apiUserId": self.api_user_id,     # API User ID
                "apiKey": self.api_key,            # API Key
                "paymentMethod": "MWALLET_ACCOUNT",
                "payerInfo": {
                    "accountNo": payer_account  # Payer phone number
                },
                "transactionInfo": {
                    "referenceId": reference_id,   # Unique referenceId
                    "invoiceId": self.invoice_id,       # Invoice ID
                    "amount": str(amount),         # Amount
                    "currency": currency,          # Currency (default is USD)
                    "description": description     # Description (default is "test")
                }
            }
        }

        # Convert payload to JSON string
        payload_json = json.dumps(payload)

        # Send the POST request with the JSON payload
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.base_url, data=payload_json, headers=headers)

        # Return the response for further processing
        return response.json()

    def preauthorize_commit(self, transaction_id, description="Committed"):
        # Prepare the request payload
        payload = {
            "schemaVersion": "1.0",
            "requestId": self.request_id,  # Share the same requestId
            "timestamp": self.timestamp,     # Share the same timestamp
            "channelName": "WEB",
            "serviceName": "API_PREAUTHORIZE_COMMIT",
            "serviceParams": {
                "merchantUid": self.merchant_uid,  # Merchant UID
                "apiUserId": self.api_user_id,     # API User ID
                "apiKey": self.api_key,            # API Key
                "paymentMethod": "MWALLET_ACCOUNT",
                "transactionId": transaction_id,    # Transaction ID from preauthorize
                "description": description           # Description
            }
        }

        # Convert payload to JSON string
        payload_json = json.dumps(payload)

        # Send the POST request with the JSON payload
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.base_url, data=payload_json, headers=headers)

        # Return the response for further processing
        return response.json()

    def preauthorize_cancel(self, transaction_id, description="Cancelled"):
        # Prepare the request payload
        payload = {
            "schemaVersion": "1.0",
            "requestId": self.request_id,  # Share the same requestId
            "timestamp": self.timestamp,     # Share the same timestamp
            "channelName": "WEB",
            "serviceName": "API_PREAUTHORIZE_CANCEL",
            "serviceParams": {
                "merchantUid": self.merchant_uid,  # Merchant UID
                "apiUserId": self.api_user_id,     # API User ID
                "apiKey": self.api_key,            # API Key
                "paymentMethod": "MWALLET_ACCOUNT",
                "transactionId": transaction_id,    # Transaction ID to cancel
                "description": description           # Description
            }
        }

        # Convert payload to JSON string
        payload_json = json.dumps(payload)

        # Send the POST request with the JSON payload
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.base_url, data=payload_json, headers=headers)

        # Return the response for further processing
        return response.json()
